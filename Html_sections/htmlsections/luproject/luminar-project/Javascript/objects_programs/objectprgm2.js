var employ={
    id:100,ename:"Ajay",exp:2,salary:40000
}

//printing salary
if("salary" in employ){
    console.log(employ.salary);
}

//print name

if("ename" in employ){
    console.log(employ.ename);
}
else{
    console.log("key error");
}

//check gender key

if("gender" in employ){
    console.log("key exists");
}
else{
    employ["gender"]="male";
}
console.log(employ);

//if employee salary is <40000 then add 5000 more

if(employ["salary"]<=40000){
    employ["salary"]+=5000;
}
console.log(employ);

