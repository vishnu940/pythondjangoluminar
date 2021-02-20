from re import *

f=open("vehiclenumbers","r")
for lines in f:
    words=lines.rstrip("\n").split(",")
    #print(words)

    for word in words:
        rule='KL-\d{2}-[a-zA-Z]{1,2}-\d{0,4}'
        matcher=fullmatch(rule,word)

        if(matcher==None):
            print("invalid vehicle numbers")
        else:
            print("valid vehicle numbers:",word)


