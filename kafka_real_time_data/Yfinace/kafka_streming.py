import os
from pyspark.sql import SparkSession

# কম মেমোরি সেটিংস সহ Spark কনফিগারেশন
os.environ['PYSPARK_SUBMIT_ARGS'] = '--packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.4 --driver-memory 2g --executor-memory 2g pyspark-shell'

# Spark সেশন তৈরি করুন
spark = SparkSession.builder \
    .appName("KafkaIntegration") \
    .getOrCreate()

# Kafka থেকে ডেটা পড়ুন
df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "customer_activities") \
    .load()

# মানকে স্ট্রিং-এ রূপান্তর করুন
json_df = df.selectExpr("CAST(value AS STRING)")

# কনসোলে আউটপুট দেখান
query = json_df.writeStream \
    .outputMode("append") \
    .format("console") \
    .start()

query.awaitTermination()