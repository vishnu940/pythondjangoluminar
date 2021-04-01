var arry=[1,2,3,4,5,7];
var low=0;
var up=arry.length-1;
var num=4;
while(low<up){
    tot=arry[low]+arry[up];
    if(num==tot){
        console.log(arry[low],arry[up]);
        break;
    }
    else if(num>tot){
        low=low+1;
    }
    else{
        up=up-1;
    }
}