package ir.mfozouni;

public class AppConfig {
    final static String applicationID ="HelloProducer";
    final static String bootstrapServers ="localhost:9092,localhost:9093,localhost:9094";
    final static String topicName ="hello-producer";
    final static int numEvents =500000;
}
