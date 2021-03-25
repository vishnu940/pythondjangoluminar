//objects program
//objects same as dictionary

var employee={
    id:1001,name:"haris",desig:"develeper",salary:25000
}

//console.log(employee);

//printing employee name

//console.log(employee["name"]);
//console.log(employee.name);
//printing employee id

//console.log(employee["id"]);
//console.log(employee.id);

//checking for gender key
//console.log("gender" in employee);

//adding gender key

employee["gender"]="male"
console.log(employee);

for(let key in employee){
    console.log(key);
}
