import pyodbc
import snowflake.connector
import pandas as pd

# SQL Server configuration
sql_server_config = {
    'server': 'your_sql_server',
    'database': 'your_database',
    'username': 'your_username',
    'password': 'your_password'
}

# Snowflake configuration
snowflake_config = {
    'user': 'your_snowflake_user',
    'password': 'your_snowflake_password',
    'account': 'your_snowflake_account',
    'warehouse': 'your_warehouse',
    'database': 'your_snowflake_database',
    'schema': 'your_snowflake_schema'
}

# Connect to SQL Server
conn_sql_server = pyodbc.connect(
    f"DRIVER={{SQL Server}};SERVER={sql_server_config['server']};DATABASE={sql_server_config['database']};UID={sql_server_config['username']};PWD={sql_server_config['password']}"
)

# Define the query to fetch data
query = "SELECT * FROM your_table"

# Extract data from SQL Server
df = pd.read_sql(query, conn_sql_server)

# Close the SQL Server connection
conn_sql_server.close()

# Connect to Snowflake
conn_snowflake = snowflake.connector.connect(
    user=snowflake_config['user'],
    password=snowflake_config['password'],
    account=snowflake_config['account'],
    warehouse=snowflake_config['warehouse'],
    database=snowflake_config['database'],
    schema=snowflake_config['schema']
)

# Define the Snowflake table name
snowflake_table = 'your_snowflake_table'

# Create a cursor object
cur = conn_snowflake.cursor()

# Load data into Snowflake
# Create a Snowflake table if it doesn't exist
create_table_query = f"""
CREATE OR REPLACE TABLE {snowflake_table} (
    column1 TYPE,
    column2 TYPE,
    ...
)
"""
cur.execute(create_table_query)

# Insert data into Snowflake table
# You may need to adjust the INSERT statement based on your table schema
insert_query = f"INSERT INTO {snowflake_table} (column1, column2, ...) VALUES (%s, %s, ...)"
cur.executemany(insert_query, df.values.tolist())

# Commit the transaction
conn_snowflake.commit()

# Close the Snowflake connection
cur.close()
conn_snowflake.close()

print("ETL process completed successfully.")
