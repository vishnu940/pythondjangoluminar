from re import *

email=input("Enter the email id")

rule='[.a-zA-Z]+[\d]*@gmail.com'

matcher=fullmatch(rule,email)

if matcher==None:
    print("invalid email id")
else:
    print("valid email id")
