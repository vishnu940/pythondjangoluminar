#read two numbers
#print true if sum of two number is equal to 100 or any number is 100
#else print false

#num1=int(input("Enter 1st no:"))
#num2=int(input("Enter 2nd no:"))
#sum=num1+num2
#print("sum=",sum)
#if(sum>=100):
#    print("it is true")
#elif(num1 & num2==100):
#    print("it is true")
#else:
#    print("it is false")


num1=int(input("Enter 1st no:"))
num2=int(input("Enter 2nd no:"))
if((num1+num2==100)|(num1==100)|(num2==100)):
    print("true")
else:
    print("false")


