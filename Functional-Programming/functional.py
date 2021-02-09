#program to add tow numbers using function

# def add(n1,n2):
#     return n1+n2
#
# data=add(5,2)
# print(data)


#Functional programming is used to reduce the line of codes

#lamda

#addition,multiplication,subtraction using lambda function

# add=lambda n1,n2:n1+n2
#
# print(add(5,2))

# mul=lambda n1,n2:n1*n2
#
# print(mul(5,2))

# sub=lambda num1,num2:num1-num2
# print(sub(20,5))

#cube of a number
cube=lambda num:num**3
print(cube(5))

#check even number or not

even=lambda num:num%2==0
print(even(12))


#print the square of numbers in the list
# lst=[2,4,5,6,7]
# lst1=[]
# for num in lst:
#     srt=num**2
#     lst1.append(srt)
# print(lst1)


#using map function

lst=[1,2,3,4,5,6]

def square(num):
    return num**2

sqlist=list(map(square,lst))
#function,iterables
print(sqlist)