var students=[
    [1,"David","BCA",300],
    [2,"Haris","BCA",200],
    [3,"John","BCA",400],
    [4,"Jacob","MCA",400],
    [5,"Johnson","MCA",200],
    [6,"Joseph","MCA",300],
]

//console.log(students);

for(std of students){
    console.log(std);
}

//print total marks

var total=0;
for(std of students){
    total=total+std[3];
}
console.log(`Total of marks:${total}`);

//print student name whose mark>200

for(std of students){
    if(std[3]>200){
        console.log(std[1]);
    }
}

//print total of bca and mca

var bctot=0;
var mctot=0;
for(std of students){
    if(std[2]=="BCA"){
        bctot=bctot+std[3];
    }
    else{
        mctot=mctot+std[3];
    }
}
console.log(`Bca Total:${bctot}`);
console.log(`Mca Total:${mctot}`);

//check if mark>200 pass else fail
var pass_std=[];
for(std of students){
    if(std[3]>200){
        pass_std.push(std[1])
    }
}
console.log(`Passed students`);
console.log(pass_std);

//print the name of mca students
var m_std=[];
for(std of students){
    if(std[2]=="MCA"){
        m_std.push(std[1]);
    }
}
console.log(`Mca Students:`);
console.log(m_std);

//find the average marks

var tot=0;
for(std of students){
    tot=tot+std[3];
}
console.log(`Total marks:${tot}`);

var avg=0;
avg=tot/6;
console.log(avg);