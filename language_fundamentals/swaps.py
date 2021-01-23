#program to swap two numbers
#Swapping using a temporary variable
#num1=input("Enter no1:")
#num2=input("Enter no2:")
#temp=0
#temp=num1
#num1=num2
#num2=temp
#print("Swapped values are:")
#print(num1)
#print(num2)
#Swapping without a temporary variable

num1=int(input("Enter no1:"))
num2=int(input("Enter no2:"))
num1=num1+num2
num2=num1-num2
num1=num1-num2
print(num1)
print(num2)