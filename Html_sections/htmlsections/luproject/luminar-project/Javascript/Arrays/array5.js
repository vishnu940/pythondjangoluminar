var arry=[[10,20],[21,22],[51,52],[53,54,55,56]];
//console.log(arry);
var arry2=[];
for(sub of arry){
    for(ar of sub){
        arry2.push(ar);
    }
}
console.log(arry2);