from re import *

phonenum=(input("Enter your mobile number:"))

#rule="[+][9][1][0-9]*"
rule='(91)?\d{10}'
matcher=fullmatch(rule,phonenum)
if matcher==None:
    print("invalid phone number")
else:
    print("valid phone number")
