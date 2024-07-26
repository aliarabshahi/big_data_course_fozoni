### Set Hostnames in WSL (a mini DNS server):

```bash
$ sudo nano /etc/hosts

127.0.0.1	kafka0
127.0.0.1	kafka1
127.0.0.1	kafka2
```
### Now, we try Zookeeper:

```bash
$ cd ~/kafka/kafka_2.13-3.7.0

$ nano config/zookeeper.properties

dataDir=/home/amin/kafka/data_zookeeper/zookeeper

$ bin/zookeeper-server-start.sh config/zookeeper.properties
```

### Creating and configuring a 3 nodes cluster by hand:

```bash
$ cd ~/kafka/kafka_2.13-3.7.0
$ cp config/server.properties config/server0.properties
$ cp config/server.properties config/server1.properties
$ cp config/server.properties config/server2.properties
```

```bash
$ nano config/server0.properties
	broker.id=0
	listeners=PLAINTEXT://kafka0:9093
	log.dirs=/home/amin/kafka/data_zookeeper/kafka-logs-0
```

```bash
$ nano config/server1.properties
	broker.id=1
	listeners=PLAINTEXT://kafka1:9094
	log.dirs=/home/amin/kafka/data_zookeeper/kafka-logs-1
```

```bash
$ nano config/server2.properties
	broker.id=2
	listeners=PLAINTEXT://kafka2:9095
	log.dirs=/home/amin/kafka/data_zookeeper/kafka-logs-2
```

### Start your cluster and have fun:

```bash
$ cd ~/kafka/kafka_2.13-3.7.0
$ bin/kafka-server-start.sh config/server0.properties
$ bin/kafka-server-start.sh config/server1.properties
$ bin/kafka-server-start.sh config/server2.properties
```

### Check the cluster:

```bash
# The jps command lists the instrumented Java HotSpot VMs on the target system.
$ jps

# The process ID numbers for each
# instance are on the left and will likely be different each time you run the start scripts and the host name is on the right. 
```

### Check something:

```bash
$ kafka-topics.sh --bootstrap-server kafka0:9093 --create  --topic eventsTopic  --partitions 4 --replication-factor 2

$ kafkacat -b kafka0:9093 -L -t eventsTopic

$ kafkacat -b kafka2:9095 -L -t eventsTopic
```

### Stop one broker and check what will happen:

Go to command line and terminate (ctrl + c) server_0. Now:

```bash
$ kafkacat -b kafka1:9094 -L -t eventsTopic
```

### Produce and Consume some contents by Python:

```bash
$ cd ./codes

$ python3 user_event_producer.py

$ python3 user_event_consumer.py

$ kafkacat -C -b kafka1:9094 -t eventsTopic -J
```

