from confluent_kafka import Consumer, KafkaError
import json
import pandas as pd
import os

# Kafka Consumer Configuration
kafka_config = {
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'stock_group',
    'auto.offset.reset': 'earliest'
}
consumer = Consumer(kafka_config)
consumer.subscribe(['stock_data'])

# CSV file path
csv_file_path = 'stock_data.csv'

# Function to write data to CSV
def write_to_csv(stock_data):
    # Convert JSON to DataFrame
    df = pd.DataFrame([stock_data])
    
    # Check if the file exists
    if not os.path.isfile(csv_file_path):
        # Write the DataFrame to a new CSV file
        df.to_csv(csv_file_path, index=False)
    else:
        # Append the data to the existing CSV file
        df.to_csv(csv_file_path, mode='a', header=False, index=False)

# Consume messages and write to CSV
while True:
    msg = consumer.poll(1.0)
    if msg is None:
        continue
    if msg.error():
        if msg.error().code() == KafkaError._PARTITION_EOF:
            continue
        else:
            print(msg.error())
            break
    stock_data = json.loads(msg.value().decode('utf-8'))
    print(f"Received data: {stock_data}")
    
    # Write the received data to CSV
    write_to_csv(stock_data)
