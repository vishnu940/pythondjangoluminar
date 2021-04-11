var st1=["David","Harry","Kiran","John","Kiran","Joseph"]
var st2=["David","Harry"];

for(std1 of st1){
    for(std2 of st2){
        if(std1==std2){
            console.log(std2);
        }
    }
}

// var std1=new Set(st1);
// var std2=new Set(st2);
// var pass_st=new Set([...std1].filter(x=>!std2.has(x)));
// console.log(pass_st);