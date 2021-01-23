employees=[
    [10,"christy","dataanalyst",50000],
    [11,"jhon","ba",30000],
    [12,"sab","dataanalyst",40000],
    [13,"tom","developer",40000],
    [14,"jhoni","developer",30000],
    [15,"sabir","dataanalyst",50000],
    [16,"tino","developer",40000],
    [17,"tomis","developer",47000],
    [18,"jhonis","developer",32000],
]
#print the number of emloyees in this company

num_of_employ=len(employees)
print("No:of employees=",num_of_employ)

#print how much salaries company has to raise in the month end

total=0
for emp in employees:
    total+=emp[3]
print("Total salary amount=",total)

#groupby designation wise

da=0
dv=0
b=0
for emp in employees:
    if(emp[2]=="dataanalyst"):
        da=da+1
    elif(emp[2]=="ba"):
        b=b+1
    else:
        dv=dv+1
print("Total number of data analyst=",da)
print("Total number of ba=",b)
print("Total number of developers=",dv)

#print highest salaried employee name

salary_list=[]
for emp in employees:
    salary_list.append(emp[3])
high=max(salary_list)
print(high)
for emp in employees:
    if(emp[3]==high):
        salary_list.append(employees)
        print(emp)
#print employee name who recieves lowest salaray whose designation =developer

sal_list=[]
for emp in employees:
    sal_list.append(emp[3])
low=min(sal_list)
print(low)
for emp in employees:
    if((emp[3]==low) & (emp[2]=="developer")):
        sal_list.append(employees)
        print(emp)