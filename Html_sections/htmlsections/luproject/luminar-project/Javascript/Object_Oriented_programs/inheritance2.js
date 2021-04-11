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
class Subchild extends Child{
    m3(){
        console.log("inside subchild class");
    }
}

var obj=new Subchild();
obj.m1();
obj.m2();
obj.m3();
