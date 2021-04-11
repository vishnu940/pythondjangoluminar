var clk=document.querySelector("#clk");

clk.addEventListener("click",()=>{
    clk.textContent="clicked";
    clk.style.color="red";
})
 
var dlk=document.querySelector("#dlk");

dlk.addEventListener("dblclick",()=>{
    dlk.textContent="double clicked";
    dlk.style.color="brown";
})

var mover=document.querySelector("#mso");

mover.addEventListener("mouseover",()=>{
    mover.textContent="mouse over me";
    mover.style.color="blue";
})

mover.addEventListener("mouseout",()=>{
    mover.textContent="mouse not over me";
    mover.style.color="gray";
})