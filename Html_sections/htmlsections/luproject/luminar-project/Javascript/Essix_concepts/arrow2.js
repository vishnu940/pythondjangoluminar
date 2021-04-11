var arry=[30,20,10,40,11,12,13,14,15,41,42,43];

//print even numbers

arry.filter(num=>num%2==0).forEach(num=>console.log(num));

//print odd numbers

//arry.filter(num=>num%2!=0).forEach(num=>console.log(num));

//sort the array

// arry.sort((no1,no2)=>no2-no1);
// console.log(arry);

//arry.sort((no1,no2)=>no2-no1).forEach(num=>console.log(num));

//arry.sort((num1,num2)=>num1>num2?-1:1).forEach(num=>console.log(num));

arry.sort((num1,num2)=>num1<num2?-1:1).forEach(num=>console.log(num));