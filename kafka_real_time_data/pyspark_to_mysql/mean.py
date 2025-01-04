from pyspark.sql import SparkSession

# Create a Spark session
spark = SparkSession.builder \
    .appName("ETL with Swiggy Cleaned Data") \
    .getOrCreate()

# Database connection properties
jdbc_url = "jdbc:mysql://localhost:3306/hotel_offers"
properties = {
    "user": "root",
    "password": "12345",
    "driver": "com.mysql.cj.jdbc.Driver"
}

# Extract data from the swiggy_cleaned table
df = spark.read.jdbc(url=jdbc_url, table="swiggy_cleaned", properties=properties)

# Transform data
# Example transformation: filter hotels with a rating above 4 and offers above a certain amount
transformed_df = df.filter((df["rating"] > 4) & (df["offer_above"] > 100)) \
                   .select("hotel_name", "rating", "time_minutes", "food_type", "location", "offer_above", "offer_percentage")

# Load the transformed data back to a SQL database or another destination
transformed_df.write.jdbc(url=jdbc_url, table="filtered_swiggy_offers", mode="overwrite", properties=properties)

# Stop the Spark session
spark.stop()