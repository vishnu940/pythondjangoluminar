import mysql.connector

db=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Password@123",
    database="mydatabase",
    auth_plugin="mysql_native_password"

)

cursor=db.cursor()
try:
    sql="insert into films values(3,'batman','2008',4.5)"
    cursor.execute(sql)
    print("records inserted")
    db.commit()
except Exception as e:
    print(e.args)
    db.rollback()
db.close()