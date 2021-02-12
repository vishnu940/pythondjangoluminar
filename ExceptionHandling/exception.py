#Exception handling,helps to handle errors
#Exception occurs during the exexuction of the program and it disrupts the normal,
# flow of program instruction

#Exception handling keywords:
#try,except,finally
#Excep
n1=int(input())
n2=int(input())
try:
    res=n1/n2
    print(res)
except Exception as e:
    print("Exception occured")
print("i have file operation")
print("i have created database")

#try block represents:
#try=> doubtful code try
#except block represents how to handle error

