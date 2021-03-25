// arrays
//insertion order preserved 
//duplicates allowed
//homogeneous and hetrogenious data

// var array=[10,"hello",true,20.2,"hai"];
// console.log(array);

//var numbers=[10,20,30,40,50];
//console.log(numbers[2]);
// for(let i=0;i<numbers.length;i++){
//     console.log(numbers[i]);
// }

// for(let num of numbers){
//     console.log(num);
// }
//to add an element to array use push

//numbers.push(100);
//console.log(numbers);

//to delete an element from array use pop

//numbers.pop();
//console.log(numbers);

//var array1=[10,20,30,40];
//var array2=[21,22,30,31,40];
// for(let i of array1){
//     for(let j of array2){
//         if(i==j){
//             console.log(i);
            
//         }
//     }
// }

//By using algorithm
//Algorithm
//if array1[element1]==array2[element2]
//element1++
//element2++
//if array1[element1]<array2[element2]
//element1++
//if array1[element1]>array2[element2]
//element2++


var array1=[10,20,30,40];
var array2=[21,22,30,31,40];
var array3=[];
var i=0;
var j=0;


// while((i<array1.length) && (j<array2.length)){
//     if(array1[i]==array2[j]){
//         array3.push(array1[i]);
//         console.log(array1[i]);
//         i++;
//         j++;
//         }
//     else if(array1[i]<array2[j]){
//         i++;
//         }
//     else{
//         j++;
//         }

//     }


while((i<array1.length) && (j<array2.length)){//0<4 && o<5
    if(array1[i]==array2[j]){//
        array3.push(array1[i]);
        console.log(array1[i]);
        i++;
        j++;
    }
    else if(array1[i]<array2[j]){
        i++;
    }
    else{
        j++;
    }
}