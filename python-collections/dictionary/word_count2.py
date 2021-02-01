#count no;of words hello and welcome

text="hello welcome hello welcome"
words=text.split(" ")
dict={}
for word in words:
    if(word not in dict):
        dict[word]=1
    else:
        dict[word]+=1
print(dict)
