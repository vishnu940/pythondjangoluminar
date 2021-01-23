#read three numbers and find the highest number
#find second largest number 40
#sort these three numbers


#num1=int(input("Enter no1:"))
#num2=int(input("Enter no2:"))
#num3=int(input("Enter no3:"))
#if((num1>num2) & (num1>num3)):
#    print(mum1,"is highest")
#elif((num2>num1) & (num2>num3)):
#    print(num2,"is highest")
#elif((num3>num1) & (num3>num2)):
#    print(num3,"is highest")
#elif((num1==num2) & (num1==num3)):
#    print("3 numbers are equal")


num1=int(input("Enter no1:"))
num2=int(input("Enter no2:"))
num3=int(input("Enter no3:"))
if (num1>num2) & (num1>num3):
    print(num1,"is highest")
    #num1 is the highest in this code block
    #possibility for second largest num is either num1 or num2
    if(num2>num3):
       print("second largest is",num2)
       print("sorted order",num1,num2,num3)
    elif(num3>num2):
       print("second largest is",num3)
       print("sorted order is",num1,num3,num2)
    elif(num2==num3):
        print("num2,num3",num2,num3)
elif (num2>num1) & (num2>num3):
    print(num2,"is highest")
    if(num1>num3):
       print("second largest is",num1)
       print("sorted order is",num2,num1,num3)
    elif(num3>num1):
       print("second largest is",num3)
       print("sorted order is",num2,num3,num1)
    elif(num1==num3):
       print("num1,num3",num1,num3)
elif(num3>num1) & (num3>num2):
     print(num3,"is highest")
     if(num1>num2):
         print("second largest is",num1)
         print("sorted order is",num3,num1,num2)
     elif(num2>num1):
         print("secondlargest is",num2)
         print("sorted order is",num3,num2,num1)
     elif(num1==num2):
         print("num1,num2",num1,num2)

elif(num1==num2) & (num1==num3):
    print("3 numbers are equal")
