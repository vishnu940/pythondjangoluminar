#create a class and open the file in the class

#print student details whose course is mca

#no of students as mca and bca

#print students details who have highest mark

#print students details who have lowest mark


#implement map,filter function


class Student:
    def __init__(self,roll,name,course,mark):
        self.roll=roll
        self.name=name
        self.course=course
        self.mark=mark

    def __str__(self):
        return self.name

f=open("student","r")
stdlst=[]
for lines in f:
    id,nme,crs,mrk=lines.rstrip("\n").split(",")
    obj=Student(id,nme,crs,mrk)
    stdlst.append(obj)

for std in stdlst:
    if std.course=="mca":
        print(std)

high=max(list(map(lambda mrk:mrk.mark,stdlst)))
print(high)

low=min(list(map(lambda mrk:mrk.mark,stdlst)))
print(low)

mk=list(filter(lambda name:name.course=="mca",stdlst))
for m in mk:
    print(m)