#Implementing constructor

class Employ:

    def __init__(self,id,nam,ds):
        self.id=id
        self.name=nam
        self.desig=ds

    def print_employ(self):
        print(self.id,self.name,self.desig)

obj=Employ(1024,"Employee1","BA")
obj.print_employ()

obj1=Employ(1026,"Employee2","PG")
obj1.print_employ()