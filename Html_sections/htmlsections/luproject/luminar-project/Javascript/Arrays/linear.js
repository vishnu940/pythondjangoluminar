var arry=[10,11,12,13,14,15,16];
var flag=0;
var num=14;
for(i of arry){
    if(num==i){
        flag=flag+1;
        break;

    }
}
if(flag==0){
    console.log("Element not found");
}
else{
    console.log("Element found");
}