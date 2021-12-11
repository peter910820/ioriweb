window.onload =  ShowTime();

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
/*===================================================== */
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
function ShowTime(){
  var NowDate=new Date();
  var h=NowDate.getHours();
  var m=NowDate.getMinutes();
  var s=NowDate.getSeconds();
  document.getElementById('showbox').innerHTML = h+'時'+m+'分'+s+'秒';
  setTimeout('ShowTime()',1000);
  }
/*===================================================== */

