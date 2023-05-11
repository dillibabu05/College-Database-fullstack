$(document).ready(function(){
  $('#birth-date').mask('00/00/0000');
  $('#phone-number').mask('0000-0000');
 })


// *******************form validation *******************
//name....password...email...phone...
function btn_1(){
  var username=document.getElementById('user_name').value;
  if (username==""){
    document.getElementById('demo').innerHTML="please enter your name";
  }
}