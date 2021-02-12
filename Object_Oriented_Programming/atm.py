# class Bank:
#     def bal_enq(self):
#         print("inside balance enquiry")
#
#     def withdraw(self):
#         print("inside withdraw")
#
#     def __deposit(self):#declaring __deposit as a private method
#         print("inside deposit")
#         #self.__deposit()#Accesing deposit inside the class
#
# class Atm(Bank):
#     pass
#
# a=Atm()
# a.bal_enq()
# a.withdraw()
# a._Bank__deposit()#calling the value of private method




class Bank:
    def bal_enq(self):
        print("inside balance enquiry")
    def withdraw(self):
        print("inside withdraw")
    def __deposit(self):
        print("inside deposit")

obj=Bank()
obj._Bank__deposit()
obj.withdraw()
obj.bal_enq()
