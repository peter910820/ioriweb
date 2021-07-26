window.onload = function(){ 
  var audio = document.getElementById('music');
      audio.pause();
}
function play() {
   var audio = document.getElementById('music');
   if (audio.paused) {
       audio.play();
   }else{
       audio.pause();
       audio.currentTime = 0;
   }
}

function toggle1() {
  document.getElementById('menu').style.overflowY='scroll';
  }
function toggle2() {
  document.getElementById('menu').style.overflowY='hidden';
}