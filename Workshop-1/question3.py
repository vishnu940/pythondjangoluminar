#Power Ranger
#Given 3 inputs n, minimum, & maximum, find the number of values raised to the nth power that lie in the range
# [minimum, maximum], inclusive.

num=int(input("Enter number:"))
min=int(input("Enter minimum value:"))
max=int(input("Enter maximum value:"))
for i in range(1,max+1):
    if i**num in range(min,max):
        print(i)