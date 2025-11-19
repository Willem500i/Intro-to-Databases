import mysql.connector
from mysql.connector import Error
from config import Config

def get_db_connection():
    """Create and return a database connection"""
    try:
        connection = mysql.connector.connect(
            host=Config.MYSQL_HOST,
            port=Config.MYSQL_PORT,
            user=Config.MYSQL_USER,
            password=Config.MYSQL_PASSWORD,
            database=Config.MYSQL_DATABASE
        )
        return connection
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        print(f"Attempted connection to: {Config.MYSQL_USER}@{Config.MYSQL_HOST}:{Config.MYSQL_PORT}/{Config.MYSQL_DATABASE}")
        return None

def execute_query(query, params=None, fetch=True):
    """Execute a query and return results"""
    connection = get_db_connection()
    if not connection:
        return None
    
    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute(query, params or ())
        
        if fetch:
            results = cursor.fetchall()
        else:
            connection.commit()
            results = cursor.rowcount
        
        cursor.close()
        return results
    except Error as e:
        print(f"Error executing query: {e}")
        connection.rollback()
        return None
    finally:
        if connection.is_connected():
            connection.close()

def execute_prepared_query(query, params=None, fetch=True):
    """Execute a prepared statement query"""
    connection = get_db_connection()
    if not connection:
        return None
    
    try:
        # mysql-connector-python uses cursor.execute() with parameterized queries for prepared statements
        cursor = connection.cursor(dictionary=True)
        cursor.execute(query, params or ())
        
        if fetch:
            results = cursor.fetchall()
        else:
            connection.commit()
            results = cursor.rowcount
        
        cursor.close()
        return results
    except Error as e:
        print(f"Error executing prepared query: {e}")
        connection.rollback()
        return None
    finally:
        if connection.is_connected():
            connection.close()

