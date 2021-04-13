var employee=[
    {id:1000,Name:"Ajay",salary:25000,exp:1},
    {id:1001,Name:"Vijay",salary:30000,exp:2},
    {id:1002,Name:"David",salary:35000,exp:2},
    {id:1003,Name:"Haris",salary:30000,exp:2},
]

//printing salary
for(let emp of employee){
    if("salary" in emp){
        console.log(emp.salary);
    }
}

//print the name of employee whose id=1001

for(let emp of employee){
    if(emp["id"]==1001){
        console.log(emp.Name);
    }
}
//print the salary of employee whose id=1003

for(let emp of employee){
    if(emp["id"]==1003){
        console.log(emp.salary);
    }
}

//add address 

for(let emp of employee){
    if("Address" in emp){
        console.log("Exist");
    }
    else{
        emp["Address"]="kochi";
        //console.log(emp);

    }
}

//change address of id 1002

for(let emp of employee){
    if(emp["id"]==1002){
        emp["Address"]="Mumbai";
        console.log(emp);
    }
}

//change the address of id 1001

for(let emp of employee){
    if(emp["id"]==1001){
        emp["Address"]="Banglore";
        console.log(emp);
    }
}