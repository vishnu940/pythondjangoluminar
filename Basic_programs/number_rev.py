#program to find reverse of a number

rev=0
num=int(input("Enter the number:"))#123
while(num>0):#123>0
    digit=num % 10#123%10=12.3,
    num=num//10#12.3=1
    print(digit, end="")
