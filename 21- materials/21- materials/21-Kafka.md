# Postgres, kafka and Ksqldb

### Build the connect image (if you want to upgrade versions):

```bash
$ docker build -t debezium-connect -f debezium.Dockerfile .

# See inside the debezium.Dockerfile file to see where and how we get jdbc files. Note that jdbc means "Java™ database connectivity". 
```

### Bring up the entire environment:

Set the following dns in your host files (windows or linux):

127.0.0.1 postgres
127.0.0.1 schema-registry
127.0.0.1 kafka
127.0.0.1 connect
127.0.0.1 ksql-server
127.0.0.1 zookeeper

```bash
$ docker-compose up -d
```

### Loading data into Postgres:

We will bring up a container with a psql command line, mount our local data files inside, create a database called `students`, and load the data on students' chance of admission into the `admission` table.

```bash
$ psql -h postgres -U postgres
```

Password = postgres

```bash
$ CREATE DATABASE students;
$ \connect students;
```

##### 🛑 We can open our pgAdmin4 to see the process in a GUI. But it's more time consuming!

Load our admission data table:

```bash
$ CREATE TABLE admission
(student_id INTEGER, gre INTEGER, toefl INTEGER, cpga DOUBLE PRECISION, admit_chance DOUBLE PRECISION,
CONSTRAINT student_id_pk PRIMARY KEY (student_id));

$ \copy admission FROM '/home/config/admit.csv' DELIMITER ',' CSV HEADER
```

Load the research data table with:

```bash
$ CREATE TABLE research
(student_id INTEGER, rating INTEGER, research INTEGER,
PRIMARY KEY (student_id));

$ \copy research FROM '/home/config/research.csv' DELIMITER ',' CSV HEADER
```

### Connect Postgres database as a source to Kafka:

```bash
$ docker ps --format "table {{.ID}} ----- {{.Names}}"

$ docker exec -it <kafka-container-id> /bin/bash

$ /usr/bin/kafka-topics --list --zookeeper zookeeper:2181
```

The postgres-source.json file contains the configuration settings needed to sink all of the students database to Kafka.

```bash
$ curl -X POST -H "Accept:application/json" -H "Content-Type: application/json" \
--data @./postgres-source.json http://connect:8083/connectors
```

```bash
$ curl -H "Accept:application/json" connect:8083/connectors/
```

```bash
$ /usr/bin/kafka-topics --list --zookeeper zookeeper:2181
```

### Create tables in KSQL:

Bring up a KSQL server command line client as a container (in windows. In linux instead of a backtick " ` " we should use of " \ "):

```bash
$ docker run --network session_13_default `
           --interactive --tty --rm `
           confluentinc/cp-ksql-cli:5.1.2 `
           http://ksql-server:8088
```

To see your updates, a few settings need to be configured by first running:

```bash
$ set 'commit.interval.ms'='2000';
$ set 'cache.max.bytes.buffering'='10000000';
$ set 'auto.offset.reset'='earliest';
```

### Some notes:

![](.\postgres_and_docker\layers2.png)

![](.\postgres_and_docker\layers.png)

### Mirror Postgres tables:

The Postgres table topics will be visible in KSQL, and we will create KSQL streams to auto update KSQL tables mirroring the Postgres tables:

```bash
$ SHOW TOPICS;

$ CREATE STREAM admission_src (student_id INTEGER, gre INTEGER, toefl INTEGER, cpga DOUBLE, admit_chance DOUBLE)\
WITH (KAFKA_TOPIC='dbserver1.public.admission', VALUE_FORMAT='AVRO');

$ CREATE STREAM admission_src_rekey WITH (PARTITIONS=1) AS \
SELECT * FROM admission_src PARTITION BY student_id;

$ SHOW STREAMS;

$ CREATE TABLE admission (student_id INTEGER, gre INTEGER, toefl INTEGER, cpga DOUBLE, admit_chance DOUBLE)\
WITH (KAFKA_TOPIC='ADMISSION_SRC_REKEY', VALUE_FORMAT='AVRO', KEY='student_id');

$ SHOW TABLES;

$ DESCRIBE admission;

$ CREATE STREAM research_src (student_id INTEGER, rating INTEGER, research INTEGER)\
WITH (KAFKA_TOPIC='dbserver1.public.research', VALUE_FORMAT='AVRO');

$ CREATE STREAM research_src_rekey WITH (PARTITIONS=1) AS \
SELECT * FROM research_src PARTITION BY student_id;

$ CREATE TABLE research (student_id INTEGER, rating INTEGER, research INTEGER)\
WITH (KAFKA_TOPIC='RESEARCH_SRC_REKEY', VALUE_FORMAT='AVRO', KEY='student_id');
```

### Create downstream tables:

We will create a new KSQL streaming table to join students' chance of admission with research experience.

```bash
$ CREATE TABLE research_boost AS \
  SELECT a.student_id as student_id, \
         a.admit_chance as admit_chance, \
         r.research as research \
  FROM admission a \
  LEFT JOIN research r on a.student_id = r.student_id;
```

And another table calculating the average chance of admission for students with and without research experience:

```bash
$ CREATE TABLE research_ave_boost AS \
     SELECT research, SUM(admit_chance)/COUNT(admit_chance) as ave_chance \
     FROM research_boost \
     WITH (KAFKA_TOPIC='research_ave_boost', VALUE_FORMAT='delimited', KEY='research') \
     GROUP BY research;
```



Add a connector to sink a KSQL table back to Postgres

The postgres-sink.json configuration file will create a RESEARCH_AVE_BOOST table and send the data back to Postgres.

```bash
$ curl -X POST -H "Accept:application/json" -H "Content-Type: application/json" \
      --data @postgres-sink.json http://connect:8083/connectors
```

### Update the source Postgres tables and watch the Postgres sink table update:

The RESEARCH_AVE_BOOST table should now be available in Postgres to query:

```bash
$ \dt

$ SELECT "AVE_CHANCE" FROM "RESEARCH_AVE_BOOST"
  WHERE cast("RESEARCH" as INT)=0;
```

```bash
$ SELECT * FROM  RESEARCH_AVE_BOOST LIMIT 5;
```

With these data the average admission chance will be 65.19%.

```bash
$ INSERT INTO admission (student_id , gre , toefl , cpga , admit_chance) VALUES (301,313,120, 9, 0.99);
```

### Exercise: 

Do the instructions in the following article step-by-step and carefully:

[Stream Processing and Data Analysis with ksqlDB](https://towardsdatascience.com/stream-processing-and-data-analysis-with-ksqldb-97f1ca4fcf6a )

### Appendix (URLs which you encounter in the video):

1- [Index of maven/io/confluent/kafka-connect-jdbc](http://packages.confluent.io/maven/io/confluent/kafka-connect-jdbc/)

2- [confluent.hub](https://www.confluent.io/hub/)

3- [Kafka Calculator (estimate the size of your cluster)](https://eventsizer.io/)

4- [Alopeyk Data Architecture](https://www.aparat.com/v/6zH9K)

![Data architecture of Alopeyk](.\postgres_and_docker\layers3-Aloopeyk.jpg)

![](.\postgres_and_docker\layers4-aloopeyk2.jpg)