from kafka import KafkaProducer
import json
import time

# Initialize Kafka producer
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Send data to Kafka every 5 seconds
while True:
    data = {'activity': 'purchase', 'customer_id': 123, 'amount': 49.99}
    producer.send('customer_activities', value=data)
    print(f"Sent: {data}")
    time.sleep(5)