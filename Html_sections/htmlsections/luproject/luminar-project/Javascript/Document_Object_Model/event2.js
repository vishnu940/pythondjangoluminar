var mclk=document.querySelector("#clk");

mclk.addEventListener("click",()=>{
    mclk.textContent="clicked";
    mclk.style.color="red";
})

var dclk=document.querySelector("#dlk");
 dclk.addEventListener("dblclick",()=>{
     dclk.textContent="double clicked";
     dclk.style.color="brown";
 })
 var ms=document.querySelector("#mso");
 ms.addEventListener("mouseover",()=>{
     ms.textContent="mouse over me";
     ms.style.color="green";
 })
 ms.addEventListener("mouseout",()=>{
     ms.textContent="mouse not over me";
     ms.style.color="grey";
 })