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
//for(emp of employees){
 //    console.log(emp);
 //}

//print the number of employees

var num_emp=employees.length;
console.log(`No:of employees:${num_emp}`);

//print the total of salary
var total=0;
for(emp of employees){
    total+=emp[3];
    
}
console.log(`total salary:${total}`);

//print the designation wise details

var devp=0;
var ba=0;
var da=0;

for(emp of employees){
    if(emp[2]=="developer"){
        devp=devp+1;
    }
    else if(emp[2]=="dataanalyst"){
        da=da+1;
    }
    else{
        ba=ba+1;
    }
}
console.log(`No:of developers:${devp}`);
console.log(`No:of data analyst:${da}`);
console.log(`No:of business analyst:${ba}`);

//print the highest salary
var sal_lst=[];
for(emp of employees){
    sal_lst.push(emp[3])
}
//console.log(sal_lst);
var high_sal=Math.max(...sal_lst);
console.log(`Highest salary:${high_sal}`);

//print the highest salaried employee name
for(emp of employees){
    if(emp[3]==high_sal){
        sal_lst.push(employees);
        console.log(`Highest salaried employee:${emp[1]}`);
    }
}
//print employee name who recieves lowest salaray whose designation=developer

var arry=[];
for(emp of employees){
    arry.push(emp[3]);
}
var low_sal=Math.min(...arry);
//console.log(low_sal);

for(emp of employees){
    if(emp[3]==low_sal & emp[2]=="developer"){
        arry.push(employees);
        console.log(`Lowest salaried employee in developer ${emp[1]}`);
    }
}