var num=6;
var flag=0;

for(let i=2;i<num;i++){
    if(num%i==0){
        flag=flag+1;
        break;
    }
    else{
        flag=0;
    }
}
if(flag==0){
    console.log(`${num} is prime`);
}
else{
    console.log(`${num} is not prime`);
}
