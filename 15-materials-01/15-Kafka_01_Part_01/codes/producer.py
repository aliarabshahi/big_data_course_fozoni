from time import sleep
from json import dumps
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers=['localhost:9092'], value_serializer=lambda x: dumps(x).encode('utf-8'))

# The value_serializer parameter specifies how the producer should
# serialize the values of the records before sending them to the Kafka cluster.
# In this case, it is set to a lambda function that serializes
# the values as JSON strings and encodes them as UTF-8 byte strings.

for e in range(1000):
 data = {'number' : e}
 producer.send('numbers', value=data)
 print(f"Sending data : {data}")
 sleep(1)
