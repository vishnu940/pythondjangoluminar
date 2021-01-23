#lst=[10,8,7,11,12,6,5]

#element=12
#step1 sort this list
#[5,6,7,8,10,11,12]
# 0 1 2 3  4  5  6
# l      mid        u
#calculate mid=(lower+upper)//2=0+6//2=3
#mid=3
#conditions:
#if(element>lst[mid]) print low=mid+1

lst=[10,8,7,11,12,6,5]
lst.sort()
flag=0
low=0
high=len(lst)-1
num=int(input("Enter the element to search:"))
while(low<=high):
    mid=(low+high)//2
    if(num>lst[mid]):
        low=mid+1
    elif(num<lst[mid]):
        hign=mid-1
    elif(num==lst[mid]):
        flag=flag+1
        break
if(flag==0):
    print("Element not found")
else:
    print("Element found")

