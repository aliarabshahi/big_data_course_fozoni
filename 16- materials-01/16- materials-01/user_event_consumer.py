import json
from kafka import KafkaConsumer

TOPIC_NAME = 'numbers'

consumer = KafkaConsumer(
    TOPIC_NAME,
    auto_offset_reset='earliest', 
    group_id='event-collector-group-1',
    bootstrap_servers=['localhost:9092','localhost:9094','localhost:9096'],
    value_deserializer=lambda m: json.loads(m.decode('utf-8')) ,
    security_protocol= 'PLAINTEXT'
)

def consume_events():
    for message in consumer:
        print(f"Partition:{message.partition}\tOffset:{message.offset}\tKey:{message.key}\tValue:{message.value}")

if __name__ == '__main__':
    print("Consumer Started ...")
    consume_events()