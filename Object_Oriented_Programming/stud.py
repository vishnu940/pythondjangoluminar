class Std:

    def __init__(self):
        print("No values")

    def __init__(self,name,age):
        self.name=name
        self.age=age

        print("Name:",self.name)
        print("Age:",self.age)


obj=Std("David",25)

#constructor overloading is not supported