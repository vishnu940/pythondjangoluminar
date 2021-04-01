var arry=[2,5,6,7];
var total=0;
var sum=[];
for(num of arry){
    total=total+num;
}
console.log(`Total:${total}`);

for(tot of arry){
    tot=total-tot;
    sum.push(tot)
}
console.log(sum);