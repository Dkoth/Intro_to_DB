import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connecting to the MySQL server 
        connection = mysql.connector.connect(
            host="localhost",     
            user="your_username",  
            password="your_password"  
        )

        if connection.is_connected():
            # Creating a cursor object to execute SQL queries
            cursor = connection.cursor()

            # Creating the alx_book_store database if it doesn't exist
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")
    except mysql.connector.Error as e:
        print(f"Error while connecting to MySQL: {e}")
    
    finally:
        # Ensuring the connection is closed  
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed.")

# Calling  the function to create the database 
create_database()
