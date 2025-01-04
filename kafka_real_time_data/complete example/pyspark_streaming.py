from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, StructField, StringType, FloatType, IntegerType

# Initialize Spark session with Kafka integration
spark = SparkSession.builder \
    .appName("KafkaSparkMySQL") \
    .config("spark.jars.packages", "org.apache.spark:spark-sql-kafka-0-10_2.12:3.4.0") \
    .getOrCreate()

# Define the schema of the incoming JSON data
schema = StructType([
    StructField("activity", StringType(), True),
    StructField("customer_id", IntegerType(), True),
    StructField("amount", FloatType(), True)
])

# Read data from Kafka
kafkaDF = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "customer_activities") \
    .load()

# Process the data
processedDF = kafkaDF.selectExpr("CAST(value AS STRING)") \
    .select(from_json(col("value"), schema).alias("data")) \
    .select("data.*")

# Function to write to MySQL
def write_to_mysql(batch_df, batch_id):
    batch_df.write \
        .format("jdbc") \
        .option("url", "jdbc:mysql://localhost:3306/your_database") \
        .option("dbtable", "customer_activity_table") \
        .option("user", "your_user") \
        .option("password", "your_password") \
        .mode("append") \
        .save()

# Start the streaming query
query = processedDF.writeStream \
    .outputMode("append") \
    .foreachBatch(write_to_mysql) \
    .trigger(processingTime='10 seconds') \
    .start()

query.awaitTermination()