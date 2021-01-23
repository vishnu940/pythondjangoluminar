#read lower limit and upper limit
#print all even numbers from this lower limit to upper limit

#lower=int(input("Enter the lower limit:"))
#upper=int(input("Enter the upper limit:"))
#n=1
#for n in range(lower,upper):
#    if(n%2==0):
#        print(n)
#    n+=1

lower=int(input("Enter lower limit:"))
upper=int(input("Enter upper limit:"))
while(lower<=upper):
    if(lower%2==0):
        print(lower)
    lower+=1
