class Student{
    stdata(roll,cors,name){
        this.roll=roll;
        this.cors=cors;
        this.name=name;
    }
    printdata(){
        console.log("Rollno:"+this.roll);
        console.log("Course:"+this.cors);
        console.log("Name:"+this.name);
    }
}
var obj=new Student()
obj.stdata(10236,"Mca","Vijay");
obj.printdata();

var obj2=new Student()
obj2.stdata(12360,"Bca","Haris");
obj2.printdata();