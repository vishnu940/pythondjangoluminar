employ={"id":100,"ename":"ajay","exp":2,"salary":35000}
if("salary" in employ):
    print(employ["salary"])

#print employee name

print(employ["ename"])
#check for gender pair

if("gender" in employ):
    print("exist")
else:
    #print("not exist")
    employ["gender"]="male"
print(employ)

#if employee salary is <35000 then add 5000 more

if(employ["salary"]<=35000):
    employ["salary"]+=5000
print(employ)