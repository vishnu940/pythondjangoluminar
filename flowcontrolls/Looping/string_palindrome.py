#program to reverse a string

#name="luminar"
#length=len(name)-1
#while(length>=0):
#    print(name[length],end="")
#    length-=1

name="luminar"
length=len(name)-1
reverse=""
while(length>=0):
    reverse+=name[length]
    length-=1
print(reverse)