#print year wised released movies
#count no:of movies released in each year also count the maximum movies released in which year

f=open("movies.csv","r")
dict={}
for lines in f:
    data=lines.rstrip("\n").split(",")
    mname=data[1]
    yr=int(data[2])
    if(mname not in dict):
        dict[mname]=yr
    else:
        dict[mname]=yr
for k,v in dict.items():
    print(k,"===>",v)




