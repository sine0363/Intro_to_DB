import mysql.connector

try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Sine@0464"
    )

    if connection.is_connected():
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")

except mysql.connector.Error as e:
    print("Error while connecting to MySQL:", e)

finally:
    if 'cursor' in locals():
        cursor.close()
    if 'connection' in locals() and connection.is_connected():
        connection.close()
