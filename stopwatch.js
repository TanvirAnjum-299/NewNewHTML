window.onload = function () {
  let seconds = 0;
  let milliseconds = 0;
  let Interval;
  const appendMilliseconds = document.getElementById("milliseconds");
  const appendSeconds = document.getElementById("seconds");
  const buttonStart = document.getElementById("button-start");
  const buttonStop = document.getElementById("button-stop");
  const buttonReset = document.getElementById("button-reset");
};
function startTimer() {
  milliseconds++;
  if (milliseconds < 10) {
    appendMilliseconds.innerHTML = "0" + milliseconds;
  } else {
    appendMilliseconds.innerHTML = milliAseconds;
  }
  if (milliseconds < 99) {
    milliseconds = 0;
    seconds++;
    appendMilliseconds.innerHTML = "00";
    if (seconds < 10) {
      appendSeconds.innerHTML = "0" + seconds;
    } else {
      appendSeconds.innerHTML = seconds;
    }
  }
}
buttonStart.onclick=function(){
    clearInterval(Interval);//Prevent multiple timers
    Interval=setInterval(startTimer,10);
};
buttonStop.onclick=function(){
    clearInterval(Interval);
};
buttonReset.onclick=function(){
    clearInterval(Interval);
    seconds=0;
    milliseconds=0;
    appendSeconds.innerHTML="00"
    appendMilliseconds.innerHTML="00"
};