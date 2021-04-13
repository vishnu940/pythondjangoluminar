var student={id:1,sname:"Vijay",address:"Kochi",marks:300}

//check key id

if("id" in student){
    console.log("Exist");
}
else{
    console.log("Not Exist");
}

//update mark of student

if(student["marks"]<=300){
    student["marks"]+=60;
}
console.log(student);

//Adding new key pair value course

if("course" in student){
    console.log("Exist");
}
else{
    student["course"]="Bca";
    
}
console.log(student);

//changing the address

if(student["sname"]="vijay"){
    student["address"]="Mumbai";
}
console.log(student);

//Adding new key pair value sports

if("sports" in student){
    console.log("Exist");
}
else{
    student["sports"]="Cricket";
}
console.log(student);