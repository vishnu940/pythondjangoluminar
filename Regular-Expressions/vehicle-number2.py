#validate vehicle register number

from re import *

venum=input("Enter the vehicle number:")

#rule="KL-\d{2}-[a-zA-Z]{2}-\d{4}"
rule='KL-\d{2}-[a-zA-Z]{1,2}-\d{0,4}'
mathcer=fullmatch(rule,venum)

if mathcer==None:
    print("invalid vehicle number")
else:
    print("valid vehicle number")