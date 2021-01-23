#print all even numbers upto this limit

#limit=int(input("Enter the limit:"))
#n=1
#while(n<=limit):#1<=5 2<=5 3<=5 4<=5 5<=5 6<=5
#    if(n%2==0):#1%2==0 2%2==0 3%2==0 4%2==0 5%2==0
#        print(n)#2 4
#    n+=1#i=2 3 4 5 6


l=int(input("Enter the limit:"))
n=1
while(n<=l):
    if(n%2!=0):
        print(n)
    n+=1