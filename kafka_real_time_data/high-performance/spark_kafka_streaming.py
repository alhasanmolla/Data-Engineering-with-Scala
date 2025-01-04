from pyspark.sql import SparkSession
from pyspark.sql.functions import col

def main():
    spark = SparkSession.builder \
        .appName("Kafka Spark Streaming") \
        .master("local[*]") \
        .config("spark.jars.packages", "org.apache.spark:spark-sql-kafka-0-10_2.12:3.1.1") \
        .getOrCreate()

    kafka_topic = "customer_activities"
    
    # Read stream from Kafka
    kafka_stream = spark.readStream \
        .format("kafka") \
        .option("kafka.bootstrap.servers", "localhost:9092") \
        .option("subscribe", kafka_topic) \
        .load()

    # Select key and value
    processed_data = kafka_stream.selectExpr("CAST(key AS STRING)", "CAST(value AS STRING)")

    # Write stream to console (for debugging; change to your desired sink)
    query = processed_data.writeStream \
        .outputMode("append") \
        .format("console") \
        .start()

    query.awaitTermination()

if __name__ == "__main__":
    main()