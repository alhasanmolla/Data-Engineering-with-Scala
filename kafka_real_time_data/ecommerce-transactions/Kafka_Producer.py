from kafka import KafkaProducer
import json
import time
import random

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda x: json.dumps(x).encode('utf-8')
)

# Simulated transaction data
products = [
    {"product_id": 1, "category": "Electronics", "price": 500},
    {"product_id": 2, "category": "Books", "price": 20},
    {"product_id": 3, "category": "Clothing", "price": 50},
]

try:
    while True:
        product = random.choice(products)
        transaction = {
            "transaction_id": random.randint(1000, 9999),
            "user_id": random.randint(1, 100),
            "product_id": product["product_id"],
            "category": product["category"],
            "price": product["price"],
            "quantity": random.randint(1, 5),
            "timestamp": time.time()
        }
        producer.send('customer_activities', value=transaction)
        print(f"Sent: {transaction}")
        time.sleep(1)
except KeyboardInterrupt:
    print("Producer stopped.")
finally:
    producer.close()