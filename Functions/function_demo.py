#functions are used to perform aparticulaar task
#unctions are called using function name
#Functions include
#print()
#len()
#lstrip()
#rstrip()
#split()
#type()
#sum()
#creating function:
#def function_name(param1,param2,param3):
   #  function defenition
#function_name()

#function without passing parameters

#def add():
#    a=int(input("Enter 1st no:"))
#    b=int(input("Enter 2nd no:"))
#    c=a+b
#    print("addition=",c)
#add()

#function with passing parameters

#def add(a,b):
#    c=a+b
#    print("Addition=",c)
#    return c
#num1=int(input("Enter 1st no:"))
#num2=int(input("Enter 2nd no:"))
#add(num1,num2)

def mult(x,y):
    z=x*y
    return z
n1=int(input("Enter 1st no:"))
n2=int(input("Enter 2nd no:"))
print("Product=",mult(n1,n2))

def cube(num):
    return num**3
data=cube(2)
print(data)
#A parameter is the variable listed inside the parentheses in the function defenition