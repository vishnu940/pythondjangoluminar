lst=[[10,20],[21,22],[51,52],[53,54,55,56]]
#print [10 20 21 22 51 52 53 54 55 56]

x=[]
for sub in lst:
    for num in sub:
        x.append(num)
print(x)