class Parent{
    phone(){
        console.log("Parent phone");
    }
}
class Child extends Parent{
    phone(){
        console.log("Child phone method");
    }
}
var obj=new Child();
obj.phone();