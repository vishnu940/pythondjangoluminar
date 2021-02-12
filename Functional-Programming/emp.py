#print employee details whose designation is developer

#no of employees as developer

#print employee details who have highest salary


class Employ:
    def __init__(self,id,name,desig,exp,salary):
        self.eid=id
        self.ename=name
        self.desig=desig
        self.exp=exp
        self.salary=salary

    def __str__(self):
        return self.ename


f=open("employ","r")
elist=[]
sallst=[]

for lines in f:
    eid,ename,desig,exp,salary=lines.rstrip("\n").split(",")
    elist.append(Employ(eid,ename,desig,exp,salary))
    # obj=Employ(eid,ename,desig,exp,salary)
    # elist.append(obj)


# for emp in elist:
#     if emp.desig=="developer":
#         print(emp.ename)
#using fliter function

# nm=list(filter(lambda name:name.desig=="developer",elist))
# for emp in nm:
#     print(emp)

#print the numbers of developers

# high=len(list(filter(lambda n:n.desig=="developer",elist)))
# print(high)

#print the highest salary

# highsal=max(list(map(lambda sal:sal.salary,elist)))
# print(highsal)
#
# for emp in elist:
#     if emp.desig=="developer":
#         print(emp)
#
# highsal=max(list(map(lambda sal:sal.salary,elist)))
# print(highsal)
#
#
# for emp in elist:
#     if emp.desig=="developer":
#         print(emp.ename)
#         sallst.append(emp.salary)
# print(max(sallst))
#
# for emp in elist:
#     sallst.append(emp.salary)
# print(max(sallst))


#printing the employee names in capital letter
# lst=[]
# for emp in elist:
#     lst.append(emp.ename)
# #print(lst)
# ucase=list(map(lambda name:name.upper(),lst))
# for e1 in ucase:
#     print(e1)

#print employee name who has highest salary in designation qa


for emp in elist:
    if emp.desig=="qa":
        print(emp.ename)
        sallst.append(emp.salary)
lowsal=print(max(sallst))



