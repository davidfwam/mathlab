var numberone = Math.floor(Math.random() * 1000);
var n1 = numberone.toString();
function SquareRoot(){
  var user_sum = $('#user_input').val();
  var sumofrandint = Math.floor(Math.sqrt(numberone));
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
  $(".function").append("<p> √" + n1 + " = </p>");
  $("#user_input").keydown(function(event) {

      if (event.keyCode == 13) {
        event.preventDefault();
        console.log("Got here 1");
        SquareRoot();
        }
      return true;});
 }

$(document).ready(setup)
