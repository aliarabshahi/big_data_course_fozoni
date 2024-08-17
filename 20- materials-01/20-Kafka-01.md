### Install Confluent Platform Kafka (cp-kafka)

We'll use some code snippets from this URL:

https://github.com/a0x8o/kafka/blob/master/clients/src/main/java/org/apache/kafka/common/serialization/Serdes.java

#### We use of this snippet in the process of writing custom serdes:

```java
Map<String,Object> serdeConfig = new HashMap<>();

serdeConfig.put(JsonDeserializer.VALUE_CLASS_NAME_CONFIG,PosInvoice.class);

serde.configure(serdeConfig, false);
```

