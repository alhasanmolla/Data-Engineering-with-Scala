from kafka import KafkaProducer
import json
import time
import random
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)

# Kafka producer সেটআপ
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# ব্যবহারকারীর কার্যকলাপ সিমুলেট করা
actions = ['click', 'search', 'payment', 'add_to_cart']
products = ['Laptop', 'Mobile', 'Headphones', 'Camera']
users = ['User1', 'User2', 'User3', 'User4']

try:
    while True:
        event = {
            'user': random.choice(users),
            'action': random.choice(actions),
            'product': random.choice(products),
            'timestamp': time.time()
        }
        producer.send('customer_activities', value=event)
        logging.info(f"Produced: {event}")
        time.sleep(1)  # প্রতি ১ সেকেন্ডে একটি ইভেন্ট পাঠাবে
except KeyboardInterrupt:
    logging.info("Producer stopped by user.")
finally:
    producer.close()
    logging.info("Kafka producer closed.")
