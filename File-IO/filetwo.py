#File operations:
#Read
#Write
#Append

#step 1: we have to create a reference

#writing function to open the file contents
f=open("demotwo","r")

#reading the lines in the file

#for lines in f:
#    print(lines)

word=[]
for lines in f:
    word.append(lines.rstrip("\n").split(" "))
print(word)

mywords=[]
for lst in word:
    for wrd in lst:
        mywords.append(wrd)
print(mywords)
#task
#print student name who have passed
#print repeated words from file