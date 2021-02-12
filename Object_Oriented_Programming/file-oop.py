#print employee details whose designation is developer

#no of employees as developer

#print employee details who have highest salary


class Employee:

    def __init__(self,id,name,desig,exp,salary):
        self.eid=id
        self.ename=name
        self.desig=desig
        self.exp=exp
        self.salary=salary

    def __str__(self):
        return self.ename


f=open("employees","r")
emplist=[]
sallist=[]
for lines in f:
    eid,ename,desig,exp,salary=lines.rstrip("\n").split(",")
    #emplist.append(Employee(eid,ename,desig,exp,salary))
    obj=Employee(eid,ename,desig,exp,salary)
    emplist.append(obj)

# for emp in emplist:
#     if emp.desig=="developer":
#         print(emp)

#printing highest salary of employee
# for emp in emplist:
#     sallist.append(emp.salary)
# print(max(sallist))

#printing the name of employee who has highest salary

# for emp in emplist:
#     sallist.append(emp.salary)
# higsal=max(sallist)
#
# for emp in emplist:
#     if emp.salary==higsal:
#         print(emp)
#

#counting the number of employees whose designation is developer
# count=0
# for emp in emplist:
#     if emp.desig=="developer":
#         count+=1
# print("No:of developers:",count)

#print the employee name whose has lowest salary in developer

# for emp in emplist:
#     if emp.desig=="developer":
#         print(emp)

for emp in emplist:
    if emp.desig=="developer":
        sallist.append(emp.salary)
lowsal=min(sallist)

for emp in emplist:
    if emp.salary==lowsal:
        print(emp)





            


