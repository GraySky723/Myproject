print("Hello,featuer1!")
import mysql.connector

conn = mysql.connector.connect(
    host="mysql-container",
    user="root",
    password="root",
    database="mydb"
)
