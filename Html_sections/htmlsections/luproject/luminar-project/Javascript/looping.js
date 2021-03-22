//while loop

// let i=10;
// while(i<10){
//     console.log(i);
//     i++;
//  }

// let i=10;
// while(i>0){
//     console.log(i);
//     i--;
// }

// var num=3;
// if(num%2==0){
//     console.log(num+"is even");
// }
// else{
//     console.log(num+"is odd");
// }

//check even and odd upto 50
// let num=0;

// while(num<=50){
//     if(num%2==0){
//         console.log(`number ${num} is even`);
//     }
//     else{
//         console.log(`number ${num} is odd`);
//     }
//     num++;
// }

//for loop

// for(let i=0;i<10;i++){
//     console.log(i);
// }

// for(let i=10;i>0;i--){
//     console.log(i);
// }

//prime number check

var num=23;
var flag=0;

for(let i=2;i<num;i++){
    if(num%i==0){
        flag+=1;
        break;
    }
    else{
        flag=0;
    }
    
}
if(flag==0){
    console.log(`${num} is prime`);
}
else{
    console.log(`${num} is not prime`);
}