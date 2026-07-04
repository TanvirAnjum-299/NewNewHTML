const dices=['&#9856;', '&#9857;', '&#9858;', '&#9859;', '&#9860;', '&#9861;'];
let stopped=true;
let dice;
let t;
function change(){
    const random=Math.floor(Math.random()*6);//random=0,1,2,3,4,5
    dice.innerHTML=dices[random];
}
function stopStart(){
    if(stopped){
        stopped=false;
        t=setInterval(change,1000);
    }else{
        clearInterval(t);
        stopped=true;
    }
}
window.onload=function(){
    dice=document.getElementById("dice");
    stopStart();
}