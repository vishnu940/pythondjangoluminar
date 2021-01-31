#print sum of pairs

#lst=[1,2,3,5]
#num=int(input("Enter the number:"))#3
#for i in range(0,len(lst)):#0,1
#    for j in range(i+1,len(lst)):#0+1=1,1+1=2
#        if(lst[i]+lst[j]==num):#0+1,1+2=3
#            print(lst[i],lst[j])

#different method

#lst=[1,2,3,5]
#low=0
#up=len(lst)-1
#element=int(input("Enter the element:"))
#while(low<up):
#    tot=lst[low]+lst[up]
#    if(element==tot):
#        print(lst[low],lst[up])
#        break
#    else:
#        low+=1

lst=[1,2,3,4,5,7]
low =0
up=len(lst)-1
element=int(input("Enter the element:"))
while(low<up):
    tot=lst[low]+lst[up]
    if(element==tot):
        print(lst[low],lst[up])
        break
    elif(element>tot):
        low+=1
    else:
        up-=1

