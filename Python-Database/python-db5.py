import mysql.connector

db=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Password@123",
    database="mydatabase",
    auth_plugin="mysql_native_password"
)

cursor=db.cursor()
sql="create table films(id int,name varchar(30),year varchar(30),rating int)"
cursor.execute(sql)
print("table created")
db.close()