f=open("student-file","r")
students={}
for lines in f:
    id,name,mark,course=lines.rstrip("\n").split(",")

    if id not in students:
        students[id]={"id":id,"name":name,"mark":mark,"course":course}
#print(students)

def student_data(**kwargs):
    id=kwargs["id"]
    if id in students:
        print(students[id]["name"])

        if "mrk" in kwargs:
            mrk=kwargs["mrk"]
            print(students[id][mrk])
        else:
            pass
        if "cours" in kwargs:
            cours=kwargs["cours"]
            print(students[id][cours])
        else:
            pass

    else:
        print("student value does not exists")
student_data(id="1",mrk="mark",cours="course")


