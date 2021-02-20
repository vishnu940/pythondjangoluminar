from re import *

email=input("Email id:")
rule='[a-zA-Z0-9._+%-]+@[a-zA-Z]+\.[a-zA-Z]{2,}'


matcher=fullmatch(rule,email)

if(matcher==None):
    print("invalid email")
else:
    print("valid email")