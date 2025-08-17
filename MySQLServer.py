import mysql.connector
from mysql.connector import Error

try:
    # Connect to MySQL server (use your new Python user)
    connection = mysql.connector.connect(
        host='localhost',
        user='python_user',       # replace with the user you created
        password='mypassword123'  # replace with the password you set
    )

    cursor = connection.cursor()
    
    # Create the database if it doesn't exist
    cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
    print("Database 'alx_book_store' created successfully!")

except Error as e:
    print(f"Error while connecting to MySQL: {e}")

finally:
    if 'cursor' in locals():
        cursor.close()
    if 'connection' in locals() and connection.is_connected():
        connection.close()
        print("MySQL connection closed.")
