//class->blue print,design pattern
//object->real world entity
//reference->perform operations

class Person{
    setperson(name,age){
        this.name=name;
        this.age=age;
    }
    printperson(){
        console.log(this.age+ ","+this.name);
    }
}
//object
var obj=new Person();
obj.setperson("David",25);
obj.printperson();