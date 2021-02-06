class Student:
    def set_student(self,rol,crs,nam):
        self.roll=rol
        self.course=crs
        self.name=nam

    def print_student(self):
        print("Roll-no",self.roll)
        print("Course",self.course)
        print("Name",self.name)

obj=Student()
obj.set_student(1001,"Haris","Python-Django")
# obj.print_student()
#
# obj1=Student()
# obj1.set_student(1002,"David","Python-Django")
# obj1.print_student()

print(obj.course)
print(obj.name)
print(obj.roll)

#set_student()
#initializing instance variables
#instance variables are prepended with self keyword

#we can access instance variables outside class by using reference
#we can access instance variables inside class by using self keyword

#Task:
#create Employee class
#values:eid,ename,designation,salary
#initialize
#print

#have to create minimum two objects
