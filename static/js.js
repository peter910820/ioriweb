let NowDate=new Date();
let d = NowDate.getDate();
var m = NowDate.getMonth();
var y = NowDate.getFullYear();

m = m + 1
let el2 = document.querySelector('.c');
el2.setAttribute('value', `${y}/${m}/${d}`);

window.onload =  ShowTime();

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

