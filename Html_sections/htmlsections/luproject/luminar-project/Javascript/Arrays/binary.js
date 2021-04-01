var arry=[10,8,7,11,12,6,5];
arry.sort((no1,no2)=>no1-no2)
var flag=0;
var low=0;
var high=arry.length-1;
var num=12;
while(low<=high){
    mid=(low+high)/2;
    if(num>arry[mid]){
        low=mid+1;
    }
    else if(num<arry[mid]){
        high=mid-1;
    }
    else if(num==arry[mid]){
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