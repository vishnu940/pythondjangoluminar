#find first recursive character A
#pattern="ABABBAC"
#dict={}

#for ch in pattern:
#    if ch not in dict:
#        dict[ch]=1
#    else:
#        print(ch,"recursive character")

#find first recursive character

#pattern="ABABBAC"
#dict={}
#for ch in pattern:
#    if(ch not in dict):
#        dict[ch]=1
#    else:
#        dict[ch]+=1
        #print(ch,"is the first recursive character")
        #break
#for key,value in dict.items():
#    print(key,",",value)


#find the highest frequent character

pattern="ABABBACEEEEE"
dict={}
for ch in pattern:
    if ch not in dict:
        dict[ch]=1
    else:
        dict[ch]+=1
for key,value in dict.items():
    print(key,",",value)
print(dict)
print(dict.get("E"))
srt=sorted(dict,key=dict.get)
print(srt)

#to print in reverse order
srt=sorted(dict,key=dict.get,reverse=True)
print(srt)

#to print only one item
srt=sorted(dict,key=dict.get,reverse=True)
print(srt[0])
