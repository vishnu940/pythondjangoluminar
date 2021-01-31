students=[
    [1,"David","BCA",300],
    [2,"Haris","BCA",200],
    [3,"John","BCA",400],
    [4,"Jacob","MCA",400],
    [5,"Johnson","MCA",200],
    [6,"Joseph","MCA",300],
]
#print(students)
#printing students in seperate lists

#for std in students:
#    print(std)

#print total marks of marks

#tot=0
#for std in students:
#    tot=tot+std[3]
#print(tot)

#print student name whose marks is greter than 200

#for std in students:
#    if(std[3]>200):
#        print(std[1])

#print total of bca and mca

#btot=0
#mtot=0
#for std in students:
#    if(std[2]=="BCA"):
#        btot=btot+std[3]
#    else:
#        mtot=mtot+std[3]
#print("Total BCA marks=",btot)
#print("Total MCA marks=",mtot)

#print the grade of students
#criteria is if marks >200 student pass else fail

#l2=list()
#for std in students:
#    if(std[3]>200):
#        l2.append(std[1])
#print("Passed students")
#print(l2)
#print the name of mca students only

#lst=list()
#for std in students:
#    if(std[2]=="MCA"):
#        lst.append(std)
#        print(std[1])

#find the average of marks

tot=0
for std in students:
    tot+=std[3]
print("Total=",tot)
avg=tot/6
print("Average=",avg)



