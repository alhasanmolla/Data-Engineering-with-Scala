import yfinance as yf
from confluent_kafka import Producer
import json
import time

# Kafka Producer Configuration
kafka_config = {
    'bootstrap.servers': 'localhost:9092'
}
producer = Producer(kafka_config)

# Function to fetch and send stock data to Kafka
def fetch_and_send_stock_data(symbol):
    stock = yf.Ticker(symbol)
    data = stock.history(period='1m')  # Get the latest 1-minute data
    if not data.empty:
        # Convert DataFrame to JSON and send to Kafka
        stock_data = data.tail(1).to_dict(orient='records')[0]
        producer.produce('stock_data', key=symbol, value=json.dumps(stock_data))
        producer.flush()
        print(f"Sent data for {symbol} to Kafka")

# Fetch and send data in a loop
stock_symbols = ['AAPL', 'GOOGL', 'TSLA']  # Add more symbols as needed
while True:
    for symbol in stock_symbols:
        fetch_and_send_stock_data(symbol)
    time.sleep(60)  # Wait for a minute before fetching new data
