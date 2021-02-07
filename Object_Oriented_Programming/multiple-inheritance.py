#Multiple inheritance

class Parent:
    def m1(self):
        print("inside parent1")


class Child:
    def m1(self):
        print("inside child")
class SubChild(Parent,Child):
    def m3(self):
        print("inside sub child")

obj=SubChild()
obj.m3()
obj.m1()

