#Method overriding

# class Parent:
#     def phone(self):
#         print("nokia5310")
#
# class Child(Parent):
#     def phone(self):
#         print("iphone11")
#
# obj=Child()
# obj.phone()


class Parent(object):
    def phone(self):
        print("nokia5310")

    def __str__(self):
        return "hello parent"


c=Parent()
print(c)#print an object while printing object __str__() will invoke object