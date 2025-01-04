import pandas as pd
from pyspark.sql import SparkSession
from sqlalchemy import create_engine
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import logging

# ডেটাবেস সংযোগের প্যারামিটার নির্ধারণ করুন
MYSQL_CONNECTION_STRING = 'mysql+pymysql://user:password@localhost:3306/mydatabase'  # আপনার MySQL ক্রেডেনশিয়াল দিয়ে আপডেট করুন
POSTGRES_CONNECTION_STRING = 'postgresql://user:password@localhost:5432/mydatabase'  # আপনার PostgreSQL ক্রেডেনশিয়াল দিয়ে আপডেট করুন

# একটি Spark সেশন শুরু করুন
spark = SparkSession.builder \
    .appName("MySQL to PostgreSQL ETL") \
    .getOrCreate()

# লগিং কনফিগারেশন
logging.basicConfig(level=logging.INFO)

# এক্সট্রাকশন ফাংশন নির্ধারণ করুন
def extract():
    try:
        engine = create_engine(MYSQL_CONNECTION_STRING)
        df = pd.read_sql('SELECT * FROM my_table', con=engine)  # নিশ্চিত করুন যে my_table কে আপনি যে টেবিলের সাথে কাজ করছেন তার প্রকৃত নাম দিয়ে প্রতিস্থাপন করুন
        logging.info("Data extracted successfully from MySQL.")
        return df
    except Exception as e:
        logging.error(f"Error in extraction: {e}")
        raise

# ট্রান্সফরমেশন ফাংশন নির্ধারণ করুন
def transform(df):
    try:
        spark_df = spark.createDataFrame(df)
        
        # উদাহরণ ট্রান্সফরমেশন: ৩০ এর বেশি বয়সের সারি ফিল্টার করুন
        transformed_df = spark_df.filter(spark_df.age > 30)  # আপনার স্কিমা অনুযায়ী সমন্বয় করুন
        
        logging.info("Data transformed successfully.")
        return transformed_df
    except Exception as e:
        logging.error(f"Error in transformation: {e}")
        raise

# লোডিং ফাংশন নির্ধারণ করুন
def load(spark_df):
    try:
        engine = create_engine(POSTGRES_CONNECTION_STRING)
        # লোড করার আগে Spark DataFrame কে Pandas DataFrame এ রূপান্তর করুন
        pandas_df = spark_df.toPandas()
        pandas_df.to_sql('my_table', con=engine, if_exists='replace', index=False)  # নিশ্চিত করুন যে my_table কে আপনি যে টেবিলের সাথে কাজ করছেন তার প্রকৃত নাম দিয়ে প্রতিস্থাপন করুন
        logging.info("Data loaded successfully into PostgreSQL.")
    except Exception as e:
        logging.error(f"Error in loading: {e}")
        raise

# DAG এর জন্য ডিফল্ট আর্গুমেন্ট নির্ধারণ করুন
default_args = {
    'owner': 'airflow',
    'start_date': datetime(2025, 1, 1),
    'retries': 1,
}

# DAG শুরু করুন
with DAG(
    dag_id='mysql_to_postgres_pyspark',
    default_args=default_args,
    description='PySpark ব্যবহার করে MySQL থেকে PostgreSQL এ ETL পাইপলাইন',
    schedule_interval='* * * * *',  # প্রতি মিনিটে DAG চালানোর জন্য
) as dag:

    # টাস্কগুলি নির্ধারণ করুন
    extract_task = PythonOperator(
        task_id='extract',
        python_callable=extract,
        provide_context=True,
    )

    transform_task = PythonOperator(
        task_id='transform',
        python_callable=lambda: transform(extract_task.output),
        provide_context=True,
    )

    load_task = PythonOperator(
        task_id='load',
        python_callable=lambda: load(transform_task.output),
        provide_context=True,
    )

    # টাস্কের নির্ভরতা নির্ধারণ করুন
    extract_task >> transform_task >> load_task