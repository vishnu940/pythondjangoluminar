//find the total of even and odd numbers

var arry=[10,11,12,13,14,15,16,17];
var odd=[];
var even=[];
for(num of arry){
    if(num%2==0){
        even.push(num);
        
    }
    else{
        odd.push(num);
    }
}
console.log(even);
console.log(odd);
var total=0;

for(tot of even){
    total=total+tot;
}
console.log(`Even total:${total}`);

var sum=0;
for(tot of odd){
    sum=sum+tot;
}
console.log(`Odd total:${sum}`);