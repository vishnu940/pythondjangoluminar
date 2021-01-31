#values stored in dictionary in the form key value pair
#how do we fetch value from dictionary
#is it possible to store duplicate key, key must be unique
#Example
expenses={"jan20":30000,"feb20":50000,"mar20":60000,"apr20":80000,"may20":85000}
#print(expenses["feb20"])
#check for june20
#print("june20" in expenses)

#Adding new key value pairs
#expenses["june20"]=100000
#print(expenses)
#checking for key mar20
#print("mar20" in expenses)
#updating the value of month march
expenses["mar20"]=65000
print(expenses)

expenses["mar20"]-=3000
print(expenses)