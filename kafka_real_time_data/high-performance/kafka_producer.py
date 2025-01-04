from kafka import KafkaProducer
import json
import time

def create_producer():
    return KafkaProducer(
        bootstrap_servers='localhost:9092',
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )

def produce_messages(producer, topic, num_messages):
    for i in range(num_messages):
        message = {'key': f'key-{i}', 'value': f'value-{i}'}
        producer.send(topic, value=message)
        time.sleep(0.01)  # Adjust the sleep time for desired throughput

if __name__ == "__main__":
    topic_name = "customer_activities"
    num_messages = 1200000  # Adjust for your needs

    producer = create_producer()
    produce_messages(producer, topic_name, num_messages)
    producer.close()