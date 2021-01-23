#print prime numbers in a range

#n1=int(input("Enter range1:"))
#n2=int(input("Enter range2:"))
#flag=0
#num=0
#for num in range(n1,(n2+1)):
#    for i in range(2,num):
#        if(num%i==0):
#            flag=flag+1
#            break
#        else:
#            flag=0
#    if(flag==0):
#        print(num)

lower=int(input("Enter lower limit:"))#5
upper=int(input("Enter upper limit:"))#17
flag=0
for num in range(lower,upper+1):
    for i in range(2,num):
        if(num%i==0):
            flag=flag+1
            break
        else:
            flag=0
    if(flag==0):
        print(num)


