class Student1:
    def course(self):
        print("student is studying bca")

class Student2:
    def course(self):
        print("student is studying mca")

class College:
    def start(self,study):
        study.course()

st1=Student1()
c=College()
c.start(st1)

st2=Student2()
c=College()
c.start(st2)