//student details,(name,course,place)

class Student{
    stdetails(name,course,place){
        this.name=name;
        this.course=course;
        this.place=place;
    }
    printdetails(){
        console.log(`Name:${this.name} Course:${this.course} Place:${this.place}`);
    }
}
var std=new Student();
std.stdetails("Haris","MBA","Mumbai");
std.printdetails();