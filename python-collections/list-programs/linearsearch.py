#linear search

lst=[10,11,12,13,14,15,16]
flag=0
num=int(input("Enter the element to search:"))
for i in lst:
    if(num==i):
        flag+=1
        break
    else:
        pass
if(flag==0):
    print("Element not found")
else:
    print("Element found")
