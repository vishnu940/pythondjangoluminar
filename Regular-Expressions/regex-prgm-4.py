#a,k first character must be an alphabet between a-k
#second must be a digit divisible by 3
#followed by any number of character

from re import *

varname=input("Enter the variable name")

rule="[a-kA-K][369][a-zA-Z0-9]*"

matcher=fullmatch(rule,varname)


if matcher==None:
    print("invalid variable name")
else:
    print("valid variable name")
