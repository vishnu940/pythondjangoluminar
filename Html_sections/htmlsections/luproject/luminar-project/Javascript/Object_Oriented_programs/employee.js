class Employee {
    constructor(eid, ename, desig, exp, salary) {
        this.eid = eid;
        this.ename = ename;
        this.desig = desig;
        this.exp = exp;
        this.salary = salary;
    }

}

var obj1 = new Employee(1000, "anoop", "developer", 2, 25000)
var obj2 = new Employee(1001, "sabir", "developer", 2, 40000)
var obj3 = new Employee(1002, "christy", "ba", 2, 30000)
var obj4 = new Employee(1003, "tom", "qa", 1, 20000)
var obj5 = new Employee(1004, "jack", "qa", 2, 30000)
var obj6 = new Employee(1005, "David", "ba", 2, 25000)

var elist = [];
elist.push(obj1);
elist.push(obj2);
elist.push(obj3);
elist.push(obj4);
elist.push(obj5);
elist.push(obj6);
//console.log(elist);

//print the employee name whose designation is developer

for (let emp of elist) {
    if (emp.desig == "developer") {
        console.log(emp.ename);
    }
}
//print the highest salary

var slist = [];
for (let emp of elist) {
    slist.push(emp.salary);
}
//console.log(slist);
var maxsal = Math.max(...slist)
console.log(maxsal);

//print the name of employee who has highest salary

for (let emp of elist) {
    slist.push(emp.salary);
    highsal = Math.max(...slist);
}
for (let emp of elist) {
    if (emp.salary == highsal) {
        console.log("Highest salaried employee:" + emp.ename);
    }
}

//count the no:of employees whose designation is developer

var count = 0;
for (let emp of elist) {
    if (emp.desig == "developer") {
        count += 1;
    }
}
console.log("No of Developers:" + count);

//print employee name who has lowest salary

for (let emp of elist) {
    slist.push(emp.salary)
    lowsal = Math.min(...slist);
}
for (let emp of elist) {
    if (emp.salary == lowsal) {
        console.log("Lowest salaried employee:" + emp.ename);
    }
}