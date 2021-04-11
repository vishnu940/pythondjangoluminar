class Parent{
    m1(){
        console.log("inside parent class");
    }
}
class Child extends Parent{
    m2(){
        console.log("inside child class");
    }
}

var obj=new Child();
obj.m2();
obj.m1();
