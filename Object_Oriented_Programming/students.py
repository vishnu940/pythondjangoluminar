class Students:
    def __init__(self,roll,name,course,tot):
        self.roll_no=roll
        self.name=name
        self.course=course
        self.total=tot

    # def __add__(self, other):
    #     return self.total+other.total



    def __str__(self):
        return str(self.total)





obj=Students(100,"David","Django",150)
obj1=Students(1001,"Ajay","Mean stack",140)
obj2=Students(1002,"Vijay","Django",150)


#printing the name of students whose course is Django
# stdlst=[]
#
# stdlst.append(obj)
# stdlst.append(obj1)
# stdlst.append(obj2)

# for std in stdlst:
#     #print(std)
#     if std.course=="Django":
#         print(std.name)

#print total of Django students

stlst=[]
stlst.append(obj)
stlst.append(obj1)
stlst.append(obj2)
tot=0
for std in stlst:
    if std.course=="Django":
        tot+=std.total
print(tot)
    #print(std)
