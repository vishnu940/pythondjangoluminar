#class
#object
#reference

class Person:
    #methods
    def setPerson(self,name,age):
        self.name=name
        self.age=age


    def printPerson(self):
        print("name",self.name)
        print("age",self.age)
#we created a class person(self.name,self.age)
#setPerson()
#printPerson()


obj=Person()#creating object
obj.setPerson("Vishnu",22)#calling the value
obj.printPerson()#printing the value

obj1=Person()
obj1.setPerson("Ajay",24)
obj1.printPerson()

obj2=Person()
obj2.setPerson("Vijay",26)
obj2.printPerson()

obj3=Person()
obj3.setPerson("David",28)
obj3.printPerson()



# na=input("Enter your name")
# ag=int(input("Enter your age"))
# obj.setPerson(na,ag)
# obj.printPerson()
