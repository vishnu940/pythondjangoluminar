num=int(input("Enter the number:"))
temp=num
rev=0

while(num>0):
    digit=num%10
    rev=rev+digit**3
    num=num//10

if(temp==rev):
    print("is armstrong")
else:
    print("is not armstrong")
