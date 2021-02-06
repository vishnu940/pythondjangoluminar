#program to add tow numbers using class

# class Add:
#     def add(self,a,b):
#         self.a=a
#         self.b=b
#         c=a+b
#         print("Addition=",c)
#         return c
# obj=Add()
# n1=int(input("Enter 1st no:"))
# n2=int(input("Enter 2nd no:"))
# obj.add(n1,n2)


class Add:
    def add(self,a,b):
        self.a=a
        self.b=b
        c=a+b
        print("Addition=",c)
        return c

obj=Add()
n1=int(input("Enter 1st no:"))
n2=int(input("Enter 2nd no:"))
obj.add(n1,n2)
