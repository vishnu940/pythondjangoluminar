#Find the total of list
#steps:
#find total of list
#20
#20-2=18
#20-5=15
#20-6=14
#20-7=13
#lst=[2,5,6,7]
#x=list()
#total=sum(lst)
#for i in lst:
#   x.append(total-i)
#print(x)

#finding the list of sum by taking user input
lim=int(input("Enter limit:"))
lst=list()
for i in range(0,lim):
    num=int(input("Enter number:"))
    lst.append(num)
out=list()
total=sum(lst)
for num in lst:
    out.append(total-num)
print(out)


