from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, StringType, DoubleType, TimestampType

# Step 1: Spark সেশন ইনিশিয়ালাইজ
spark = SparkSession.builder \
    .appName("KafkaConsumerWithMySQL") \
    .config("spark.jars.packages", "org.apache.spark:spark-sql-kafka-0-10_2.12:3.4.0") \
    .config("spark.jars", "mysql-connector-java-8.0.33.jar") \
    .getOrCreate()

# Step 2: Kafka কনফিগারেশন
kafka_broker = "localhost:9092"  # আপনার Kafka ব্রোকার ঠিকানাটি এখানে দিন
topic_name = "customer_activities"

# Step 3: ইনকামিং মেসেজের জন্য স্কিমা ডেফাইন করা
schema = StructType() \
    .add("user", StringType()) \
    .add("action", StringType()) \
    .add("product", StringType()) \
    .add("timestamp", DoubleType())

# Step 4: Kafka টপিক থেকে ডেটা পড়া
kafka_df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", kafka_broker) \
    .option("subscribe", topic_name) \
    .option("startingOffsets", "latest") \
    .load()

# Step 5: JSON ডেটা প্রসেস করা
parsed_df = kafka_df.selectExpr("CAST(value AS STRING)") \
    .select(from_json(col("value"), schema).alias("data")) \
    .select("data.*") \
    .withColumn("timestamp", col("timestamp").cast(TimestampType()))

# Step 6: MySQL-এ ডেটা লেখার ফাংশন
def write_to_mysql(batch_df, batch_id):
    batch_df.write \
        .format("jdbc") \
        .option("url", "jdbc:mysql://localhost:3306/customer_activity") \
        .option("driver", "com.mysql.cj.jdbc.Driver") \
        .option("dbtable", "customer_activity") \
        .option("user", "root") \
        .option("password", "12345") \
        .mode("append") \
        .save()

# Step 7: ডেটা স্ট্রিম লেখার জন্য Query শুরু করা
query = parsed_df.writeStream \
    .foreachBatch(write_to_mysql) \
    .outputMode("append") \
    .start()

# Step 8: Query এর Termination পর্যন্ত অপেক্ষা করা
query.awaitTermination()
