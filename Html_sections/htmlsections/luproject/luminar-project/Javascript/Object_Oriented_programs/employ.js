class Employ{
    emp(id,name,desig,sal){
        this.id=id;
        this.name=name;
        this.desig=desig;
        this.sal=sal;

    }
    empdetails(){
        console.log(`Employee id:${this.id} Employee name:${this.name} Designation:${this.desig} Salary:${this.sal}`);
    }

}
var obj1=new Employ()
obj1.emp(102264,"Haris","Developer",35000);
obj1.empdetails();
var obj2=new Employ()
obj2.emp(123644,"David","QA",30000);
obj2.empdetails();