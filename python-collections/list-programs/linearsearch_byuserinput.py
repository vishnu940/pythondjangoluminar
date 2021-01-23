#linear search by taking useer input

lst=list()
limit=int(input("Enter the limit:"))
for i in range(0,limit):
    element=int(input("Enter the elements:"))
    lst.append(element)
flag=0
num=int(input("Enter the element to search:"))
for j in lst:
    if(num==j):
        flag+=1
        break
    else:
        pass
if(flag==0):
    print("Element not found")
else:
    print("Element found")

