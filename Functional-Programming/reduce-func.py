from functools import reduce

lst=[2,3,4,6,8]

#printing the highest element in the list
# high=reduce(lambda n1,n2:n1 if n1>n2 else n2,lst)
# print(high)

#printing the lowest element in the list

low=reduce(lambda n1,n2:n1 if n1<n2 else n2,lst)
print(low)