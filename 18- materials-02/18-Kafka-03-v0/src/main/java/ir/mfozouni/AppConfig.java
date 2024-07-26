package ir.mfozouni;

public class AppConfig {
    final static String applicationIDProducer ="HelloProducer";
    final static String applicationIDStreams ="HelloStreams";
    final static String bootstrapServers ="localhost:9092,localhost:9093,localhost:9094";
    final static String topicName ="hello-streams";
    final static int numEvents =100;
}
