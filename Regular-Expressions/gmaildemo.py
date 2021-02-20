from re import *

em=input("Email")

rule='[a-zA-Z0-9._+%-]+@[a-zA-Z]+\.[a-zA-Z]{2,}\.[a-zA-Z]{2,}'

matcher=fullmatch(rule,em)
if matcher==None:
    print("invalid")
else:
    print("valid")