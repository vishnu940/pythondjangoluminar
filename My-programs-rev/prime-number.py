n=int(input("Enter the number"))#7
flag=0
for i in range(2,n):#2,6
    if(n%i==0):#2%2==0
        flag+=1#0=0+1
        break
    else:
        flag=0


if(flag==0):
    print("prime")
else:
    print("not prime")


