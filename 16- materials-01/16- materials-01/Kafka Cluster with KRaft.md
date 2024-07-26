### Copy KRaft server.properties

```bash
cp server.properties server-1.properties
cp server.properties server-2.properties
cp server.properties server-3.properties
```

### Configure node.id property

Each server must have a different `node.id`, regardless of its role as a `broker` or a `controller`. 

**Broker**: A Kafka broker is a server process that performs the core tasks of receiving,  storing,

 and forwarding messages within a Kafka cluster.  It acts as a node in the distributed system,

 responsible for:

- Accepting messages from producers.
- Replicating messages to followers for fault tolerance.
- Serving messages to consumers.
- Maintaining partition leadership and follower relationships.

[**Controller in KRaft Mode**](https://docs.confluent.io/platform/current/kafka-metadata/kraft.html) (Since Kafka 3.3.1): With KRaft (**Apache Kafka® Raft**), the controller functionality is distributed among a subset of brokers designated as controllers. These controllers form a quorum and use the Raft consensus protocol to agree on cluster metadata changes and elect a leader for cluster. **The leader controller is responsible for handling requests from brokers and clients, such as creating topics, assigning partitions, and changing configurations.**

![](.\Pics\KRaft-isolated-mode.png)

### Setup the id of each server

```yaml
node.id=1
# in server-1.properties file

node.id=2
# in server-2.properties

node.id=3
# in server-3.properties
```

### Configure listeners

This defines the network addresses the Kafka server uses for communication. For server 1, you’ll set it to listen on ports 9092 for Kafka broker and 9093 for the controller.

A listener is a combination of a **protocol**, a **host**, and a **port**, such as

 `listeners = PLAINTEXT://your.host.name:9092` 

The protocol defines the security mechanism for the connection, such as PLAINTEXT, SSL, SASL, etc. When the host address is omitted (represented by `:`), it signifies that the Kafka broker will listen on all network interfaces available on the machine.

```YAML
# For server-1.properties
listeners=PLAINTEXT://:9092,CONTROLLER://:9093

# For server-2.properties
listeners=PLAINTEXT://:9094,CONTROLLER://:9095

# For server-3.properties
listeners=PLAINTEXT://:9096,CONTROLLER://:9097
```

![](.\Pics\Proxy-Server.png)

### Configure advertised.listeners

```yaml
# For server-1.properties
advertised.listeners=PLAINTEXT://localhost:9092

# For server-2.properties
advertised.listeners=PLAINTEXT://localhost:9094

# For server-3.properties
advertised.listeners=PLAINTEXT://localhost:9096
```

### Log Directories

```yaml
# For server-1.properties
log.dirs=/home/amin/kafka/data_kraft/kraft-logs-1

# For server-2.properties
log.dirs=/home/amin/kafka/data_kraft/kraft-logs-2

# For server-3.properties
log.dirs=/home/amin/kafka/data_kraft/kraft-logs-3
```

### Controller Quorum Voters

Set this line in all three files server-1.properties till server-3.properties.

```yaml
controller.quorum.voters=1@localhost:9093,2@localhost:9095,3@localhost:9097
```



### Create a UUID for our Cluster

```bash
KAFKA_CLUSTER_ID="$(./bin/kafka-storage.sh random-uuid)"

echo $KAFKA_CLUSTER_ID
```

### Bind UUID to Storage

```bash
./bin/kafka-storage.sh format -t $KAFKA_CLUSTER_ID -c ./config/kraft/server-1.properties
./bin/kafka-storage.sh format -t $KAFKA_CLUSTER_ID -c ./config/kraft/server-2.properties
./bin/kafka-storage.sh format -t $KAFKA_CLUSTER_ID -c ./config/kraft/server-3.properties
```

### Start Servers

```bash
./bin/kafka-server-start.sh ./config/kraft/server-1.properties
./bin/kafka-server-start.sh ./config/kraft/server-2.properties
./bin/kafka-server-start.sh ./config/kraft/server-3.properties
```

## 4- Create a topic

```bash
kafka-topics.sh --bootstrap-server localhost:9092 --create  --topic numbers  --partitions 4 --replication-factor 1

kafkacat -b localhost:9092 -L -t numbers

kafkacat -C -b localhost:9092 -t numbers -J 
```

### Try Offsetexplorer

You can see the status of this cluster by using Offsetexplorer tool as 

```bash
cd /offsetexplorer2

./offsetexplorer

# set a name for cluster and paste the following line in Bootstarp servers
localhost:9092, localhost:9094, localhost:9096
```

## You have more question?

See this article 👇👇👇

https://www.appsdeveloperblog.com/kafka-cluster-how-to-start-3-kafka-servers-in-a-cluster/