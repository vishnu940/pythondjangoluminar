f1=open("names","r")
f2=open("faiiled","r")
dict1={}
dict2={}
for lines1 in f1:
    words1=lines1.rstrip("\n").split(" ")
    for w1 in words1:
        if(w1 not in dict1):
            dict1[w1]=1
#print(dict1)
for lines2 in f2:
    words2=lines2.rstrip("\n").split(" ")
    for w2 in words2:
        if(w2 not in dict2):
            dict2[w2]=1
#print(dict2)
st1=set(dict1)
st2=set(dict2)
passed_students=st1.difference(st2)
print("passed students:",passed_students)


