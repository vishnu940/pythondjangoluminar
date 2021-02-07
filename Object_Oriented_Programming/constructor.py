#constructor

#duty of constructor initializing instance variables
#constructor name always class name in java and c++

#In python constructor name is __init__()
#constructor automatically invoked during object creation

class Student:
    def __init__(self,ro,na,cr):
        self.roll=ro
        self.name=na
        self.course=cr

    def print_student(self):
        print("Roll-no:",self.roll)
        print("Name:",self.name)
        print("Course:",self.course)

obj=Student(102344,"David","MCA")
obj.print_student()

obj1=Student(1023655,"Haris","BCA")
obj1.print_student()
