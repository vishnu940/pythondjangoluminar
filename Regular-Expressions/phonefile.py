from re import *

f=open("phonenumbers","r")
for lines in f:
    words=lines.rstrip("\n").split(",")
    #print(words)
    for word in words:
        rule='(91)?\d{10}'
        matcher=fullmatch(rule,word)
        if(matcher==None):
            print("invalid numbers")
        else:
            print("valid numbers:",word)









