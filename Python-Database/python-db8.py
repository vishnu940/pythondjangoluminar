import mysql.connector

db=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Password@123",
    database="mydatabase",
    auth_plugin="mysql_native_password"

)

cursor=db.cursor()
sql="update films set rating=5 where id=1"
cursor.execute(sql)
print("records updated")
db.commit()
db.close()