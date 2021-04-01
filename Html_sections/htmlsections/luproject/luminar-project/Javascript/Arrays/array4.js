//program to search name

var arry=["Infosys","Tcs","Wipro","Cognizant","Ey","Sutherland"];
console.log(arry);

var flag=0;
var name="Tcs";
for(company of arry){
    if(company==name){
        flag=flag+1;
        break;
    }
}
if(flag==0){
    console.log(`company not found`);
}
else{
    console.log(`company found`);
}