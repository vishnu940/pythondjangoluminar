#find even numbers from given list using list comprehension

lst=[1,2,3,4,5,6,7,8]
# lst2=[]
# for num in lst:
#     if(num%2==0):
#         lst2.append(num)
# print(lst2)

even_lst=[num for num in lst if num%2==0]
print(even_lst)