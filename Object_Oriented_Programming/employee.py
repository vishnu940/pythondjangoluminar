#Task:
#create Employee class
#values:eid,ename,designation,salary
#initialize
#print

#have to create minimum two objects

class Employ:
    def set_employee(self,id,nam,des,sal):
        self.eid=id
        self.ename=nam
        self.desig=des
        self.salary=sal

    def print_employee(self):
        print("Employee-id:",self.eid)
        print("Employee-name:",self.ename)
        print("Employee-designation:",self.desig)
        print("Employee-salary:",self.salary)

obj=Employ()
obj.set_employee(1025566,"David","Manager",50000)
obj.print_employee()

obj1=Employ()
obj1.set_employee(1152366,"Haris","Senior Manager",80000)
obj1.print_employee()


# idd=int(input("Enter the employee id:"))
# na=input("Enter the employee name:")
# ds=input("Enter the employee designation:")
# sa=int(input("Enter the employee salary:"))
# obj.set_employee(idd,na,ds,sa)
# obj.print_employee()
