#Operator overloading

# class Book:
#     def __init__(self,pages):
#         self.pages=pages
#
#     def __add__(self, other):
#         return Book(self.pages+other.pages)
#
#
#     def __str__(self):
#         return str(self.pages)
#
# obj=Book(100)
# obj1=Book(200)
# obj2=Book(300)
# print(obj+obj1+obj2)


class Book:
    def __init__(self,pages):
        self.pages=pages


    def __add__(self, other):
        return Book(self.pages+other.pages)

    def __sub__(self, other):
        return Book(self.pages-other.pages)

    def __mul__(self, other):
        return Book(self.pages*other.pages)


    def __str__(self):
        return str(self.pages)


obj=Book(100)
obj1=Book(200)
obj2=Book(300)
print(obj+obj1+obj2)

obj=Book(100)
obj1=Book(30)
obj2=Book(20)
print(obj-obj1-obj2)

m=Book(50)
m1=Book(2)
m2=Book(3)
print(m*m1*m2)