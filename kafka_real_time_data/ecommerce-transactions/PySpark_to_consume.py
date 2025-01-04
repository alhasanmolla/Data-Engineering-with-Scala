from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum as spark_sum, count
from pyspark.sql.types import StructType, StructField, IntegerType, StringType, FloatType
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)

# Create Spark session
spark = SparkSession.builder \
    .appName("KafkaConsumer") \
    .getOrCreate()

# Define the schema for incoming data
schema = StructType([
    StructField("transaction_id", IntegerType(), True),
    StructField("user_id", IntegerType(), True),
    StructField("product_id", IntegerType(), True),
    StructField("category", StringType(), True),
    StructField("price", FloatType(), True),
    StructField("quantity", IntegerType(), True),
    StructField("timestamp", FloatType(), True)
])

# Read from Kafka
kafka_topic = "customer_activities"
kafka_bootstrap_servers = "localhost:9092"

df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", kafka_bootstrap_servers) \
    .option("subscribe", kafka_topic) \
    .load()

# Decode the value and apply the schema
value_df = df.selectExpr("CAST(value AS STRING) as json") \
    .select(from_json(col("json"), schema).alias("data")) \
    .select("data.*")

# Define aggregation logic
aggregated_df = value_df.groupBy("category").agg(
    (spark_sum(col("price") * col("quantity")).alias("total_revenue")),
    count(col("transaction_id")).alias("total_transactions")
)

# Write to MySQL
mysql_url = 'jdbc:mysql://localhost:3306/customer_activities'
properties = {
    "user": "root",
    "password": "12345",
    "driver": "com.mysql.cj.jdbc.Driver"
}

query = aggregated_df.writeStream \
    .outputMode("complete") \
    .format("jdbc") \
    .option("url", mysql_url) \
    .option("dbtable", "transaction_metrics") \
    .option("user", "root") \
    .option("password", "12345") \
    .option("truncate", "false") \
    .start()

# Await termination
query.awaitTermination()