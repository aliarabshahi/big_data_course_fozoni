package ir.mfozouni;

import org.apache.kafka.common.serialization.Serdes;
import org.apache.kafka.streams.KafkaStreams;
import org.apache.kafka.streams.StreamsBuilder;
import org.apache.kafka.streams.StreamsConfig;
import org.apache.kafka.streams.Topology;
import org.apache.kafka.streams.kstream.KStream;
import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

import java.util.Properties;

public class HelloStreams {
    private static final Logger logger = LogManager.getLogger(HelloProducer.class);
    public static void main( String[] args ){
        Properties props = new Properties();
        props.put(StreamsConfig.APPLICATION_ID_CONFIG, AppConfig.applicationIDStreams);
        props.put(StreamsConfig.BOOTSTRAP_SERVERS_CONFIG,AppConfig.bootstrapServers);
        props.put(StreamsConfig.DEFAULT_KEY_SERDE_CLASS_CONFIG, Serdes.Integer().getClass());
        props.put(StreamsConfig.DEFAULT_VALUE_SERDE_CLASS_CONFIG, Serdes.String().getClass());

        StreamsBuilder builder = new StreamsBuilder();

        KStream<Integer,String> kStream = builder.stream(AppConfig.topicName);
        kStream.foreach((k,v) -> System.out.println("Key= "+ k + " and " + "Value= " + v));

        Topology topology = builder.build();

        KafkaStreams ourStreams = new KafkaStreams(topology, props);
        logger.info("Starting ourStreams job");
        ourStreams.start();

        Runtime.getRuntime().addShutdownHook(new Thread(() -> {
            logger.info("Closing ourStreams");
            ourStreams.close();
        }));
    }
}
