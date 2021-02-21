import mysql.connector

db=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Password@123",
    database="mydatabase",
    auth_plugin="mysql_native_password"

)

def get_data():
    cursor=db.cursor()
    sql="select * from films"
    cursor.execute(sql)
    yield cursor.fetchall()

movie=get_data()
print(movie.__next__())

# for m in movie:
#     print(m)

#This concept is called generators