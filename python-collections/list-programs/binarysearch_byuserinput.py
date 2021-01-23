lst=list()

limit=int(input("Enter the limit:"))
for i in range(0,limit):
  element=int(input("Enter no:of elements:"))
  lst.append(element)
  lst.sort()
flag=0
low = 0
high =(len(lst))-1

num = int(input("Enter the element to search:"))
while(low<=high):
    mid=(low+high)//2
    if(num>lst[mid]):
       low=mid+1

    elif(num<lst[mid]):
        high=mid-1

    elif(num==lst[mid]):
        flag+=1
        break

if(flag==0):
    print("Element not found")
else:
    print("Element found")