#Read the data from the files student
#print the name and course from the file

f=open("students","r")
student={}
for lines in f:
    id,name,total,course=lines.rstrip("\n").split(",")

    if id not in student:
        student[id]={"id":id,"name":name,"total":total,"course":course}
print(student)




def print_student(**kwargs):
    id=kwargs["id"]
    if id in student:
        print(student[id]["name"])
        if "prop" in kwargs:
            prop=kwargs["prop"]
            print(student[id][prop])
    else:
        print("value not exist")

print_student(id="1001",prop="total")
