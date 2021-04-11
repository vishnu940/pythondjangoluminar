//constructor is a special method
//constructor is invoked during object creation

class Employ{
    constructor(name,desig,address){
        this.name=name;
        this.desig=desig;
        this.address=address;

    }
    printdetails(){
        console.log(`Employee name:${this.name} Designation:${this.desig} Address:${this.address}`);
    }
}
var obj=new Employ("Ajay","HR","Kochi");
obj.printdetails();