#word="hello hai hello hai hello"
#count no:of words
#hello:3,hai:2

text="hai hello hai hello"
words=text.split(" ")
#words=[hai,hello,hai,hello]

dict={}
#created an empty dictionary
#key value
#hai 1
#hello 1


for word in words:#word=hai,hello
    if(word not in dict):#if hai not in dictionary hai:1,hello:1
        dict[word]=1
    else:
        dict[word]+=1#dict["hello'] 1+1=2
print(dict)


