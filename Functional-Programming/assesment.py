employees=[
    {"id":10,"name":"christy","desig":"dataanalyst","sal":50000,"join":1980,"resign":1998},
    {"id":11,"name":"sabir","desig":"developer","sal":54000,"join":1985,"resign":1990},
    {"id":12,"name":"chris","desig":"developer","sal":30000,"join":1989,"resign":1995},
    {"id":13,"name":"david","desig":"qualityanalyst","sal":55000,"join":1990,"resign":2010},
    {"id":14,"name":"haris","desig":"businessanalyst","sal":60000,"join":1998,"resign":2012},
]
#print(employees)
#find the highest salaried employee
#print employee names whose experience >10yrs



#

# highsal=max(list(map(lambda salary:salary["sal"],employees)))
# print("highest salary:",highsal)
# for emp in employees:
#     if emp["sal"]==highsal:
#         print(emp)

# enm=list(filter(lambda ds:ds["desig"]=="businessanalyst",employees))
# print(enm)

for emp in employees:
    if "exp" not in employees:
        emp["exp"]=emp["resign"]-emp["join"]
        print(emp)

#print employees names whose experience >10yrs

# for employ in employees:
#     if employ["exp"]>10:
#         print("employee name:",employ["name"])

emexp=list((map(lambda ex:ex["exp"] if ex["exp"]>10 else ex["name"],employees)))
for employ in employees:
    if employ["exp"]>10:
        print(employ["name"])

# eexp=list(map(lambda ex:ex["name"] if ex["exp"]>10 else ex["exp"],employees))
# print(eexp)

from functools import reduce
esspp=list(filter(lambda exp:exp["exp"]==reduce(lambda ex1,ex2:ex1 if ex1>ex2 else ex2,list(map(lambda exp:exp["exp"],
                                                                                                employees))),employees))
print(esspp)












