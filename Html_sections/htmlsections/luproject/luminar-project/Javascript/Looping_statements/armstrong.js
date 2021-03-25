
var num=153;
var rev=0;
var temp=num;
while(temp>0){
    digit=temp%10;
    rev=rev+digit**3;
    temp=Math.floor(temp/10);
}

if(num==rev){
    console.log(`${num} is armstrong`);
}
else{
    console.log(`${num} is not armstrong`);
}
