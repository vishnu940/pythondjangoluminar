//var arry=[30,20,10,40,11,12,13,14,15,41,42,43];
//var tot=0;
//var arry=[1,2,3,4,5,6];

//map function
//var sqr=arry.map(num=>num**2).forEach(num=>console.log(num));

//filter function

//var even=arry.filter(num=>num%2==0).forEach(num=>console.log(num));


// for(i of arry){
//     tot=tot+i;
// }
// console.log(tot);

//reduce function

//find the sum

var arry=[30,20,10,40,11,12,13,14,15,41,42,43];

var tot=arry.reduce((num1,num2)=>num1+num2)
console.log(tot);

//find the smallest element

// var min=arry.reduce((num1,num2)=>num1<num2?num1:num2)
// console.log(min);

var min=arry.reduce((num1,num2)=>num1>num2?num2:num1);
console.log(min);