class Employ{
    constructor(eid,ename,sal,desig){
        this.eid=eid;
        this.ename=ename;
        this.sal=sal;
        this.desig=desig;
    }
    printdetails=()=>{
        console.log(this.eid+this.ename+this.sal+this.desig);
    }
}

var employ=[];
var obj1=new Employ(1,"David",33000,"Developer");
var obj2=new Employ(2,"Haris",30000,"Developer");
var obj3=new Employ(3,"Joseph",32000,"BA");
var obj4=new Employ(4,"Ajay",35000,"HR");
var obj5=new Employ(5,"Vijay",50000,"QA");
var obj6=new Employ(6,"Kiran",40000,"QA");
employ.push(obj1);
employ.push(obj2);
employ.push(obj3);
employ.push(obj4);
employ.push(obj5);
employ.push(obj6);

//printing the designation
//employ.forEach(emp=>console.log(emp.desig));

//Adding 2000 to salary

//employ.map(emp=>emp.sal+2000).forEach(sal=>console.log(sal));

//employee name in uppercase

//employ.map(emp=>emp.ename.toUpperCase()).forEach(emp=>console.log(emp));

//print employee details whose designation is developer

//employ.filter(emp=>emp.desig=="Developer").forEach(emp=>console.log(emp));

//sort employee salary wise

//employ.sort((ob1,ob2)=>ob1.sal>ob2.sal?-1:1).forEach(emp=>console.log(emp));

//employ.sort((o1,o2)=>o1.sal>o2.sal?-1:1).forEach(emp=>console.log(emp));

//sorting employee details salary wise

//employ.sort((ob1,ob2)=>ob1.sal>ob2.sal?-1:1).forEach(emp=>console.log(emp));

//Reduce function

//print highest salary 

const salary=employ.map(ob=>ob.sal).reduce((sal1,sal2)=>sal1>sal2?sal1:sal2);
console.log(salary);

//print lowest salary

const esal=employ.map(ob=>ob.sal).reduce((s1,s2)=>s1<s2?s1:s2);
console.log(esal);

