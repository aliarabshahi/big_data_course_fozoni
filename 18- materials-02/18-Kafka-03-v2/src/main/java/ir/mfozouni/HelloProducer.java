package ir.mfozouni;


import org.apache.kafka.clients.producer.KafkaProducer;
import org.apache.kafka.clients.producer.ProducerConfig;
import org.apache.kafka.clients.producer.ProducerRecord;
import org.apache.kafka.common.serialization.IntegerSerializer;
import org.apache.kafka.common.serialization.StringSerializer;
import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

import java.util.Properties;

public class HelloProducer{
    private static final Logger logger = LogManager.getLogger();
    public static void main( String[] args )
    {
        logger.info("Creating Kafka Producer");
        Properties props = new Properties();
        props.put(ProducerConfig.CLIENT_ID_CONFIG, AppConfig.applicationIDProducer);
        props.put(ProducerConfig.BOOTSTRAP_SERVERS_CONFIG, AppConfig.bootstrapServers);
        props.put(ProducerConfig.KEY_SERIALIZER_CLASS_CONFIG, IntegerSerializer.class.getName());
        props.put(ProducerConfig.VALUE_SERIALIZER_CLASS_CONFIG, StringSerializer.class.getName());

        KafkaProducer<Integer, String> producer = new KafkaProducer<>(props);

        logger.info("Start Sending Messages");

        for (int j=1; j<= AppConfig.numTries; j++) {
            for (int i = 1; i <= AppConfig.numEvents; i++) {
                producer.send(new ProducerRecord<>(AppConfig.topicName, i, "Batch " + j + " of "+ "Simple-Messages-" + i));
            }
            logger.info("Batch " + j + " sent. Waiting for 30 seconds before the next batch. Enjoy guys 😎");
             try {
                Thread.sleep(30000);
            } catch (InterruptedException e) {
                logger.error("Thread sleep interrupted: " + e.getMessage());
                Thread.currentThread().interrupt();
            }
        }

        logger.info("Closing the producer");
        producer.close();
        }
}
