#f=open("covid_19_india.csv","r")
#for lines in f:
#    data=lines.rstrip("\n").split(",")
#    print(data)
#    break

#f=open("covid_19_india.csv","r")
#for lines in f:
#    data=lines.rstrip("\n").split(",")
#    print(data)
#    break

f=open("covid_19_india.csv","r")
dict={}
for lines in f:
    data=lines.rstrip("\n").split(",")
    #state and confirmed cases
    state=data[3].rstrip("***")
    if(state=="Telengana"):
        state="Telangana"

    confirmed_cases=int(data[8])
    if(state not in dict):
        dict[state]=confirmed_cases
    else:
        dict[state]=confirmed_cases

for k,v in dict.items():
    print(k,"====>",v)
#print the states with highest cases
#res=sorted(dict,key=dict.get,reverse=True)
#print(res)
#print the state with highest case

res=sorted(dict,key=dict.get,reverse=True)
#print(res[0],dict[res[0]])
print(res[0],dict.get(res[0]))
#print(res[0],dict.get(res[0]))
#print the states in alphabetical order
#res=sorted(dict)
#print(res)