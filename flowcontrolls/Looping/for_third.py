#check given number is prime number or not

num=int(input("Enter the number:"))#suppose entering 9
flag=0
if(num==1):
    print(num,"is not prime")
else:
    for i in range(2,num):#23
       if(num%i==0):#9%2==0 953==0
          flag=flag+1#flag=flag+1
          break
       else:
          flag=0
    if(flag==0):
       print(num,"is prime")
    else:
       print(num,"is not prime")

#Assesment questions

#print prime numbers in a range



