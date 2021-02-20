from re import *

f=open("email-file","r")
for lines in f:
    words=lines.rstrip("\n").split(",")
    #print(words)
    for word in words:
        rule='[a-zA-Z0-9.+_%-]+@[a-zA-Z]+\.[a-zA-Z]{2,}'
        matcher=fullmatch(rule,word)

        if matcher==None:
            print("invalid email id")
        else:
            print("valid email id")
