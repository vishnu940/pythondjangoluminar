import mysql.connector

db=mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='Password@123',
    database='mydatabase',
    auth_plugin='mysql_native_password'

)

cursor=db.cursor()

sql="insert into movie values(1,'Avatar',2009,7.8)"
cursor.execute(sql)
print("records inserted")
db.commit()
db.close()