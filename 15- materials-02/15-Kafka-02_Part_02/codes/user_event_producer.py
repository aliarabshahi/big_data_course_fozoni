from datetime import datetime
import json
from kafka import KafkaProducer
import random
import time
import uuid

EVENT_TYPE_LIST = ['buy', 'sell', 'click', 'hover', 'idle_5']

producer = KafkaProducer(
   value_serializer=lambda msg: json.dumps(msg).encode('utf-8'), 
   bootstrap_servers=['kafka0:9093','kafka1:9094','kafka2:9095'],
   key_serializer=str.encode)

TOPIC_NAME = 'eventsTopic'


def produce_event():
    return {
        'event_id': str(uuid.uuid4()),
        'event_datetime': datetime.now().strftime('%Y-%m-%d-%H-%M-%S'),
        'event_type': random.choice(EVENT_TYPE_LIST)
    }

def send_events():
    while(True):
        data = produce_event()
        time.sleep(3)
        producer.send(TOPIC_NAME, value=data, key=data['event_id'])
        print(f"Event Created : {data['event_id']}")

if __name__ == '__main__':
    send_events()