class Employee{
    constructor(id,ename,desig,exp,sal){
        this.id=id;
        this.ename=ename;
        this.desig=desig;
        this.exp=exp;
        this.sal=sal;
    }
}
var flist=[];
var fs=require('fs');
fs.readFile('./emp.txt','utf8',function(error,data){
    //console.log(data);
    flist.push(data);
    //console.log(flist);
    for(lines of flist){
        console.log(lines);
        t
    }
   
});




