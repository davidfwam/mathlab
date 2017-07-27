var numberone = Math.floor(Math.random() * 5);
var numbertwo = Math.floor(Math.random() * 16);
var n1 = numberone.toString();
var n2 = numbertwo.toString();
function Powers(){
  var user_sum = $('#user_input').val();
  var sumofrandint = Math.pow(numbertwo, numberone);
  var usersum = Number(user_sum);

  if (sumofrandint == usersum){
    $(".response").append("<p> Congrats! Your answer is correct. </p>");
  }
  else{
    var finalsum = sumofrandint.toString();
    $(".response").append("<p> Sorry. The correct answer is " + finalsum + ".</p>");
  }
}

function setup() {
  $(".function").append("<p>" + n2 + "<sup>" + n1 + "</sup> = </p>");
  $("#user_input").keydown(function(event) {

      if (event.keyCode == 13) {
        event.preventDefault();
        console.log("Got here 1");
        Powers();
        }
      return true;});
 }

$(document).ready(setup)
