package ir.mfozouni;

import org.apache.kafka.clients.producer.KafkaProducer;
import org.apache.kafka.clients.producer.ProducerRecord;

import java.util.Properties;

public class MyClasses {
    public static void sendToKafkaTopic(String topic, Integer key, String value) {
        Properties producerProps = new Properties();
        producerProps.put("bootstrap.servers", AppConfig.bootstrapServers);
        producerProps.put("key.serializer", "org.apache.kafka.common.serialization.IntegerSerializer");
        producerProps.put("value.serializer", "org.apache.kafka.common.serialization.StringSerializer");

        KafkaProducer<Integer, String> producer = new KafkaProducer<>(producerProps);
        ProducerRecord<Integer, String> record = new ProducerRecord<>(topic, key, value);
        producer.send(record);
        producer.close();
    }
}
