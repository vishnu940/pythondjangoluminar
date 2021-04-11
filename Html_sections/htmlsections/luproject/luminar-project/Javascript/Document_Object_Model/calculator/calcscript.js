function dispbox(num){
    var tbox=document.querySelector("#txt1");
    tbox.value+=num;
    //alert("button selected");

}

function print(){
    var tbox=document.querySelector("#txt1").value;
    var eqs=eval(tbox);
    var tbox=document.querySelector("#txt1").value=eqs;
    //alert(eqs);
}

// function del(){
//     var tbox=document.querySelector("#txt1").value;
//     var data=tbox.slice(0,-1);
//     document.querySelector("#txt1").value=data;

// }

function del(){
    var tbox=document.querySelector("#txt1").value;
    var data=tbox.value="";
    document.querySelector("#txt1").value=data;
}