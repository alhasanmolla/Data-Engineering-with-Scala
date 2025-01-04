from airflow import DAG
from airflow.providers.snowflake.operators.snowflake import SnowflakeOperator
from airflow.utils.dates import days_ago

# Define default arguments
default_args = {
    'owner': 'airflow',
    'start_date': days_ago(1),
    'retries': 1,
}

# Define the DAG
with DAG(
    'snowflake_example_dag',
    default_args=default_args,
    description='A simple Snowflake DAG',
    schedule_interval='@daily',  # Modify the schedule interval based on your needs
) as dag:

    # Define the Snowflake connection parameters
    snowflake_conn_id = 'your_snowflake_connection'  # Replace with your connection ID
    sql_query = 'SELECT * FROM your_table LIMIT 10;'  # Customize the SQL query as needed

    # Snowflake Operator to execute the SQL query
    execute_query = SnowflakeOperator(
        task_id='execute_snowflake_query',
        snowflake_conn_id=snowflake_conn_id,
        sql=sql_query,
    )

    # Define task dependencies
    execute_query

# Notes
# Ensure you have the necessary permissions in Snowflake to execute the queries.
# Customize the SQL query as needed for your requirements.
# Modify the schedule interval based on your needs.
# This is a basic setup; consider adding error handling, logging, and notifications as required.

# Snowflake connection parameters (to be added in Airflow UI under Connections)
# {
#   "account": "your_account",        # Your Snowflake account
#   "warehouse": "your_warehouse",    # Your Snowflake warehouse
#   "database": "your_database",      # Your Snowflake database
#   "role": "your_role"                # Your Snowflake role
# }