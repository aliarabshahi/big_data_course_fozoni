### Install Cassandra on SparkLesson virtual Environment

```bash
$ pip install cassandra-driver --index-url https://mirrors.aliyun.com/pypi/simple/
```

### Setup Apache Cassandra first

```bash
$ docker pull cassandra:5.0

$ docker network create cn

$ docker run --name cassandra --network cn -d -p 9042:9042 cassandra:5.0

$ docker exec -it cassandra cqlsh
```

### Time Zone of Cassandra

It is in UTC. Tehran time is 3:30 ahead of it. We can create a `cqlshrc` file in and set Tehran time in that file. 

### Spark Cassandra connector

https://mvnrepository.com/artifact/com.datastax.spark/spark-cassandra-connector_2.12/3.5.1 

