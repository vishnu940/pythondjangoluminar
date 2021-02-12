# #using map function
#
# lst=[1,2,3,4,5,6]
#
# def square(num):
#     return num**2
#
# sqlist=list(map(square,lst))
# #function,iterables
# print(sqlist)


#implementing lamda function
# lst=[1,2,3,4,5,6]
#
#
# sqlist=list(map(lambda num:num**2,lst))
# print(sqlist)
#

#lst=[1,2,3,4,5,6]
# #if num<5 num-1 num>5 num+1

# nlist=list(map(lambda num:num-1 if num<5 else num+1 if num>5 else num,lst))
# print(nlist)
#


#using filter function
# lst=[1,2,3,4,5,6]
#printing even numbers from the list

# even=list(filter(lambda num:num%2==0,lst))
# print(even)

#printing odd numbers from the list

# odd=list(filter(lambda num:num%2!=0,lst))
# print(odd)

#convert all the names into uppercase
# names=["india","pak","aus","eng","sa","srilanka"]
#
# lst=list()
# for name in names:
#     name=name.upper()
#     lst.append(name)
# print(lst)

# names=["india","pak","aus","eng","sa","srilanka","auckland","indonesia"]
# ulist=list(map(lambda name:name.upper(),names))
# print(ulist)
#
# #print counry name whose letter starts with a
#
# nlist=list(filter(lambda name:name[0]=="a",names))
# print(nlist)

#reduce function

#find the sum of list
from functools import reduce #import reduce function from functools
lst=[10,11,12,13,14]
# tot=reduce(lambda n1,n2:n1+n2,lst)
# print(tot)

#print the highest number in list

# high=reduce(lambda n1,n2:n1 if n1>n2 else n2,lst)
# print(high)

#print the lowest number in list

low=reduce(lambda n1,n2:n1 if n1<n2 else n2,lst)
print(low)

#Assignment
#find the common elements from the two lists
#[1,2,3,4] [2,4,5,6,8]

l1=[1,2,3,4]
l2=[2,4,5,6,8]

s1=set(l1)
s2=set(l2)
std=s1.intersection(s2)
print(std)