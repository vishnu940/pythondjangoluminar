#find even numbers in list
#total odd numbers
#total even numbers

#x=[10,11,12,13,14,15,16,17]
#odd=list()
#even=list()
#total=0
#for num in x:
#    if(num%2==0):
#        even.append(num)

#    else:
#       odd.append(num)
#print(odd)
#print(even)
#print("Total of odd numbers:",sum(odd))
#print("tptal of even umbers:",sum(even))

x=[10,11,12,13,14,15,16,17]
odd=list()
even=list()
total=0
for i in x:
    if(i%2==0):
        even.append(i)

    else:
        odd.append(i)
print(even)
print(odd)
print("Even total=",sum(even))
print("Odd total=",sum(odd))
