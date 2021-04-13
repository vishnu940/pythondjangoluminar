class Student{
    constructor(name,course,address){
        this.name=name;
        this.course=course;
        this.address=address;
    }
    stdetails(){
        console.log(`Name:${this.name} Course: ${this.course} Address: ${this.address}`);
    }
}
var obj=new Student("Ajay","Bca","Kochi")
obj.stdetails();
var obj2=new Student("David","Mca","Kollam")
obj2.stdetails();