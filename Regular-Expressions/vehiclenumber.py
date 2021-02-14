from re import *

vnum=input("Enter the vehicle number:")
rule='KL-[0-9][0-9]-[A-Z][A-Z]-[0-9][0-9][0-9][0-9]*'
matcher=fullmatch(rule,vnum)
if matcher==None:
    print("invalid vehicle number")
else:
    print("valid vehicle number")
