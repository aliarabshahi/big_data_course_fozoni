#### Kafka has been moved to the following address:

```text
/home/amin/kafka/kafka_2.13-3.7.0
```

#### In order to work with kafka everywhere in the cli I add the path of kafka to .bashrc file as follows:

```bash
$ echo 'export PATH=/home/amin/kafka/kafka_2.13-3.7.0/bin:$PATH' >> ~/.bashrc

# run the following line to reload .bashrc file
$ source ~/.bashrc
```

#### Now, we should give execute mode to all executable files:

```
chmod +x ./bin/*
```

#### Launch Kafka with Kraft:

We can change the location of kafka log files.

- Go to KAFKA_HOME/config/kraft/server.properties

- Change the `log.dirs` parts as follows (I used absolute address):

  ```
  log.dirs=/home/amin/kafka/data_kraft/kraft-combined-logs
  ```

```bash
$ KAFKA_CLUSTER_ID="$(bin/kafka-storage.sh random-uuid)"

# you can see and check KAFKA_CLUSTER_ID variable in meta.properties file in log.dirs address.

$ bin/kafka-storage.sh format -t $KAFKA_CLUSTER_ID -c config/kraft/server.properties
$ bin/kafka-server-start.sh config/kraft/server.properties
```

### Or create a `.sh` file

```bash
#!/usr/bin/bash

KAFKA_CLUSTER_ID="$(kafka-storage.sh random-uuid)"

kafka-storage.sh format -t $KAFKA_CLUSTER_ID -c config/kraft/server.properties

kafka-server-start.sh config/kraft/server.properties
```

### Create some topics:

```bash
$ kafka-topics.sh --bootstrap-server localhost:9092 --create  --topic users  --partitions 4 --replication-factor 1

$ kafka-topics.sh --bootstrap-server localhost:9092 --list

$ kafka-topics.sh --bootstrap-server localhost:9092 --describe --topic users
```

### See some errors

```bash
$ kafka-topics.sh --bootstrap-server localhost:9092 --create  --topic users2  --partitions 4 --replication-factor 2
```

🛑 The above command will throw this error:

**Unable to replicate the partition 2 time(s): The target replication factor of 2 cannot be reached because only 1 broker(s) are registered.**

#### Produce some contents for users topic:

```bash
$ kafka-console-producer.sh --bootstrap-server localhost:9092 --property key.separator=, --property parse.key=true --topic users

$ kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic users --from-beginning  --property print.timestamp=true --property print.key=true --property print.value=true

$ kafka-console-consumer.sh --help
```

#### We can 🛑delete🛑 a topic:

```bash
$ kafka-topics.sh --bootstrap-server localhost:9092 --delete  --topic users 
```

#### Install KafkaCat:

```bash
$ sudo apt update
$ sudo apt install kafkacat
$ kafkacat -b localhost:9092 -L
```

#### Create one new topic:

```bash
$ kafka-topics.sh --bootstrap-server localhost:9092 --create  --topic numbers  --partitions 4 --replication-factor 1

$ kafkacat -b localhost:9092 -L -t numbers
```

#### Produce some contents by Python:

🛑 See the docs of kafka-python [HERE](https://kafka-python.readthedocs.io/en/master/apidoc/KafkaProducer.html).

```bash
# go to anaconda prompt cli and create a new envirenment or work on base
# my version of hafka-python is 2.0.2
$ pip install kafka-python

$ python ./codes/producer.py

# Open another console and see the comming contents
$ kafkacat -C -b localhost:9092 -t numbers

# we can see the output by more details
$ kafkacat -C -b localhost:9092 -t numbers -J

# we can see the contents of a particular partition
$ kafkacat -C -b localhost:9092 -t numbers -p 3 -J
```

#### Consume contents by Python:

```bash
$ python ./codes/consumer.py

# In order to add keys, run the following script
$ python ./codes/producer-key.py

# We can check the results by kafkacat (also)
$ kafkacat -C -b localhost:9092 -t numbers -J
```

#### One GUI for Kafka:

You can download kafka tool (offset explorer) from [HERE](https://www.kafkatool.com/download.html), or simply follow the following instruction

```bash
$ wget https://www.kafkatool.com/download3/offsetexplorer.sh

$ chmod +x offsetexplorer.sh

# Run the following command to install offsetexplorer
$ ./offsetexplorer.sh

$ cd /offsetexplorer3

$ ./offsetexplorer
```

Now, add a connection and enjoy! 😎

### Another Tool

You can work with [AKHQ](https://akhq.io/). Give it a try!