import os
from dotenv import load_dotenv
import mysql.connector
from mysql.connector import pooling


dotenv_path = '/storage/emulated/0/Python/Database/.env' 

# Load the file using the full path
load_dotenv() 

DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")
DB_PORT = int(os.getenv("DB_PORT", "3306"))

# Connection pool configuration
db_config = {
    'host': DB_HOST,
    'port': DB_PORT,
    'user': DB_USER,
    'password': DB_PASSWORD,
    'database': DB_NAME,
    'pool_name': 'railway_pool',  # Unique name for the pool
    'pool_size': 5,  # Start with 5; monitor Railway's limits
    'pool_reset_session': True,  # Reset session state for each connection 
    'connect_timeout': 10,  # Timeout for initial connection
    'autocommit': False  # Explicit commits in your code
}

# Create the connection pool
try:
    connection_pool = pooling.MySQLConnectionPool(**db_config)
    print("Connection pool created successfully.")
except mysql.connector.Error as err:
    print(f"Failed to create connection pool: {err}")
    connection_pool = None

def get_db_connection():
    if connection_pool is None:
        print("Connection pool not available.")
        return None
    
    try:
        conn = connection_pool.get_connection()
        if conn.is_connected():
            return conn
        else:
            print("Connection not active; attempting to reconnect.")
            conn.reconnect(attempts=3, delay=1)  # Retry up to 3 times with 1s delay
            return conn
    except pooling.PoolError as err:
        print(f"Pool exhausted or error: {err}")
        return None
    except mysql.connector.Error as err:
        print(f"Database connection error: {err}")
        return None
    except Exception as err:
        print(f"Unexpected error: {err}")
        return None
