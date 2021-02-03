#Nested dictionary

employee={
    1000:{"id":1000,"Name":"Ajay","salary":25000,"exp":1},
    1001:{"id":1001,"Name":"Vijay","salary":30000,"exp":2},
    1002:{"id":1002,"Name":"David","salary":35000,"exp":2},
    1003:{"id":1003,"Name":"Haris","salary":30000,"exp":2},
}
print(employee)
#print the name of employee whose id=1001
# def print_employee(id):
#     if(id in employee):
#         print(employee[id]["Name"])
# print_employee(id=1001)
#
# #print the salary of employee whose id=1003
# def print_employee(id=None):
#     if id in employee:
#         print(employee[id]["salary"])
#     else:
#         print("value does not exist")
# print_employee(id=1003)

#using **kwargs printing the list of arguements

# def print_employee(**kwargs):
#     print(kwargs)
#     id=kwargs["id"]
#     if id in employee:
#         print(employee[id]["Name"])
#
# print_employee(id=1001)

def print_employee(**kwargs):
    #print(kwargs)
    id=kwargs["id"]
    if id in employee:
        print(employee[id]["Name"])
        print(employee[id]["salary"])
        print(employee[id]["exp"])
    else:
        print("employee with this id not exist")
print_employee(id=1002)

#print the name and salary of id 1000

# def print_employee(**kwargs):
#     id=kwargs["id"]
#     if id in employee:
#         print(employee[id]["Name"])
#         if "prop" in kwargs:
#             prop=kwargs["prop"]
#             print(employee[id][prop])
#         else:
#             pass
#     else:
#         print("value does not exist")
#
# print_employee(id=1000,prop="exp")



# print(employee[1000])
# #print name of employee who's id = 1001
#
# if 1001 in employee:
#     print(employee[1001]["Name"])
# else:
#     print("Employee not exist")
#
# #print salary of 1003
#
# if 1003 in employee:
#     print("Employee salary:",employee[1003]["salary"])
#
# #add address in into 1002
#
# if("Address" in employee[1002]):
#     print("Exist")
# else:
#     employee[1002]["Address"]="kochi"
#     print(employee[1002])

