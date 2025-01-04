import json
import pandas as pd
from kafka import KafkaConsumer
from sqlalchemy import create_engine
import logging
import signal
import sys

# Setup logging
logging.basicConfig(level=logging.INFO)

# Kafka configuration
kafka_topic = "customer_activities"
kafka_bootstrap_servers = "localhost:9092"

# Create Kafka consumer
consumer = KafkaConsumer(
    kafka_topic,
    bootstrap_servers=kafka_bootstrap_servers,
    value_deserializer=lambda x: x.decode('utf-8'),
    auto_offset_reset='earliest',
    enable_auto_commit=True
)

# Initialize an empty list to hold incoming data
data_list = []

# Signal handler to gracefully shutdown
def signal_handler(sig, frame):
    logging.info("Gracefully shutting down...")
    consumer.close()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

# Read messages from Kafka
try:
    for message in consumer:
        try:
            data = json.loads(message.value)
            logging.info(f"Received data: {data}")
            data_list.append(data)
        except json.JSONDecodeError as e:
            logging.error(f"JSONDecodeError: {e} for message: {message.value}")
        except Exception as e:
            logging.error(f"Error: {e} for message: {message.value}")

        # Write to MySQL every 100 messages
        if len(data_list) >= 100:
            if data_list:
                # Filter out invalid entries
                data_list = [d for d in data_list if 'category' in d]

                # Create DataFrame
                df = pd.DataFrame(data_list)

                # Convert timestamp from float to datetime
                if 'timestamp' in df.columns:
                    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')

                # Check for 'category' column before aggregation
                if 'category' in df.columns:
                    aggregated_data = df.groupby("category").agg(
                        total_revenue=pd.NamedAgg(column="price", aggfunc=lambda x: (x * df.loc[x.index, "quantity"]).sum()),
                        total_transactions=pd.NamedAgg(column="transaction_id", aggfunc="count")
                    ).reset_index()

                    # Write to MySQL
                    mysql_url = 'mysql+pymysql://root:12345@localhost/customer_activities'
                    engine = create_engine(mysql_url)

                    try:
                        aggregated_data.to_sql('transaction_metrics', con=engine, if_exists='append', index=False)
                        logging.info("Data written to MySQL successfully.")
                    except Exception as e:
                        logging.error(f"Error writing to MySQL: {e}")

                else:
                    logging.error("The 'category' column is missing from the DataFrame.")

                # Clear the list after saving
                data_list = []
except Exception as e:
    logging.error(f"Consumer error: {e}")
finally:
    consumer.close()