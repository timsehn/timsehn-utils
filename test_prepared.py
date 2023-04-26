from mysql.connector import Error
import mysql.connector

connection = mysql.connector.connect(
    host="127.0.0.1",
    database="test_prepared",
    user="root",
    password=""
)

query="SELECT id FROM auctions WHERE ai = (SELECT ai FROM auctions ORDER BY ai DESC LIMIT 1)"

try:
    if connection.is_connected():
        cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    if result:
        print("Raw Result:")
        print(result)
    else:
        print('Not connected.')
except Error as e:
    print("Error while connecting to MySQL", e)

try:
    if connection.is_connected():
        cursor = connection.cursor(prepared=True)
    cursor.execute(query)
    result = cursor.fetchall()
    if result:
        print("Prepared Result:")
        print(result)
    else:
        print('Not connected.')
except Error as e:
    print("Error while connecting to MySQL", e)

connection.close()
