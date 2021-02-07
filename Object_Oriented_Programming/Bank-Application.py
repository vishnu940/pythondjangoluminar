#create account deposit withdrawl balance enquiry

from datetime import datetime

class Bank:
    bank_name="sbi"
    def __init__(self,acno,personnm,bal):
        self.accno=acno
        self.person_name=personnm
        self.balance=bal


    def deposit(self,amount):

        self.balance+=amount
        print("Bank-Name:",Bank.bank_name,"your account",self.accno,"has been credited with amt",amount,"on",datetime.today(),"avl bal",
              self.balance)

    def withdraw(self,amount):


        if self.balance > amount:
            self.balance-=amount
            print("Bank-Name:",Bank.bank_name,"your account", self.accno, "has been debited with amt", amount, "on", datetime.today(), "avl bal",
                  self.balance)
        else:
            print("transaction cancelled with error code")

    def balance_enquiry(self):
        print("Available balance:",self.balance)

obj=Bank(1021442364,"David",5000)
obj.deposit(7000)
obj.withdraw(5000)
obj.balance_enquiry()

obj1=Bank(202569872,"Haris",10000)
obj1.deposit(5000)
obj1.withdraw(3000)
obj1.balance_enquiry()

#different types of variables
#instance variable
#Here the variable bank_name is called as static variable or class variable
