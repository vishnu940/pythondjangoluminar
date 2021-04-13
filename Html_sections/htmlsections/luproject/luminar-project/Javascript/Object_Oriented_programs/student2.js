class Students{
    constructor(roll,sname,course,tot){
        this.roll=roll;
        this.sname=sname;
        this.course=course;
        this.tot=tot;
    }
    printdata(){
        console.log("Roll:"+this.roll);
        console.log("Name:"+this.sname);
        console.log("Course:"+this.course);
        console.log("Total:"+this.tot);
    }
    
}
var obj1=new Students(1000,"Vijay","Bca",300);
//obj1.printdata();
var obj2=new Students(1001,"Ajay","Bca",200);
//obj2.printdata();
var obj3=new Students(1003,"David","Mca",250);
//obj3.printdata();
var obj4=new Students(1004,"Jacob","Mca",350);
//obj4.printdata();

var std=[];
std.push(obj1);
std.push(obj2);
std.push(obj3);
std.push(obj4);
//console.log(std);

//print the name of students whose course is bca

for(let st of std){
    if(st.course=="Bca"){
        console.log(st.sname);
    }
}
//print total of mca students
var total=0;
for(let st of std){
    if(st.course=="Mca"){
        total+=st.tot;
                
    }
}
console.log(total);