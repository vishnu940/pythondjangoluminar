#find the squares of list

#lst=[10,20,30,40]
#using for loop
# lst2=[]
# for num in lst:
#     c=num**2
#     lst2.append(c)
# print(lst2)
#using map function
# sqr=list(map(lambda num:num**2,lst))
# print(sqr)

#using list comprehension
# sqrs=[num**2 for num in lst]
# print(sqrs)

lst=[[10,20],[30,40],[50,60]]
new_lst=[l2 for l1 in lst for l2 in l1]
print(new_lst)

#find even numbers from given list using list comprehension