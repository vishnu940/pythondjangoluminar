var students=[
    [10,"ajay","bca",250],
    [11,"vjay","bca",240],
    [12,"sibin","bca",220],
    [13,"dino","mca",220],
    [14,"tom","mca",180],
    [15,"jain","mca",250],
]
//console.log(students);

//print total of sum of total

var marks=0;

for(st of students){
    marks=marks+st[3];
}
console.log(`Total marks:${marks}`);

///print student names
var stname=[];
for(nm of students){
    stname.push(nm[1]);
}
console.log(stname);

//print students name whose total>240

for(std of students){
    if(std[3]>240){
        console.log(std[1]);
    }
}
//calculate the total of bca and mca

var tot1=0;
var tot2=0;
for(std of students){
    if(std[2]=="bca"){
        tot1=tot1+std[3];
    }
    else{
        tot2=tot2+std[3];
    }
}
console.log(`Bca total:${tot1}`);
console.log(`Mca total:${tot2}`);