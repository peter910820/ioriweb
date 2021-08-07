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

function mouseOver()
{
var x=document.getElementsByTagName("fix");
alert(x.length);
document.getElementById('fix').src ="stop.png"
}
function mouseOut()
{
document.getElementById('fix').src ="player.png"
}
/*===================================================== */

function showTime(){
  　document.getElementById('showbox').innerHTML = new Date();
  　setTimeout('ShowTime()',1000);
  }

  Today = Date();
  document.write("標準時間:<br><b>"+Today+"</b><br>");