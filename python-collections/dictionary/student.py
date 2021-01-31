student={"id":1,"sname":"Vijay","address":"Kochi","marks":300}

#checkig for key id
#if("id" in student):
#    print("exist")

#updating the marks of student
if(student["marks"]<=300):
    student["marks"]+=60
print(student)

#Adding new key pair value course
if("course" in student):
    print("Exist")
else:
    student["course"]="BCA"
print(student)
#changing the address
if(student["address"]=="Kochi"):
    student["address"]="Ernakulam"
print(student)

#Adding new key pair value sports

if("sports" in student):
    print("Exist")
else:
    student["sports"]="Football"
print(student)
