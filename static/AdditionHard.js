var numberone = Math.floor(Math.random() * 1001);
var numbertwo = Math.floor(Math.random() * 1001);
var n1 = numberone.toString();
var n2 = numbertwo.toString();
function AdditionHard(){
  var user_sum = $('#user_input').val();
  var sumofrandint = numberone + numbertwo;
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
  $(".function").append("<p>" + n1 + "+" + n2 + "= </p>");
  $("#user_input").keydown(function(event) {

      if (event.keyCode == 13) {
        event.preventDefault();
        console.log("Got here 1");
        AdditionHard();
        }
      return true;});
 }

$(document).ready(setup)
