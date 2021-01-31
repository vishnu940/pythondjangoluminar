students=[
    [10,"ajay","bca",250],
    [11,"vjay","bca",240],
    [12,"sibin","bca",220],
    [13,"dino","mca",220],
    [14,"tom","mca",180],
    [15,"jain","mca",250],
]

#print total of sum of total
marks=0
for std in students:
    marks=marks+std[3]
print("Total of marks=",marks)

#print the name of students
#for stud in students:
#    print(stud[1])

#print students name whose total>240

#for stud in students:
#    if(stud[3]>240):
#        print(stud[1])

#marks=0
#for stud in students:
#    marks=marks+stud[3]
#print("total=",marks)

#claculate total of bca and mca seperately
mtotal=0
btotal=0
for stud in students:
    if(stud[2]=="bca"):
        btotal+=stud[3]
    else:
        mtotal+=stud[3]
print("bca total:",btotal)
print("mca total:",mtotal)