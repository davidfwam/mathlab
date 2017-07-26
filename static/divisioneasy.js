var number01 = Math.floor(Math.random() * 20 + 1);
var number02 = Math.floor(Math.random() * 20 + 1);

var n01 = number01.toString();
var n02 = number02.toString();
function DivisionEasy(){
  if (number01 >= number02){
    var user_q = $('#user_input').val();
    var q = Math.floor(number01 / number02);
    var userq = Number(user_q);
    if (userq == q){
      $(".response").append("<p> Congrats! Your answer is correct. </p>");
    }
    else{
      var finalq = q.toString();
      $(".response").append("<p> Sorry. The correct answer is " + finalq + ".</p>");
    }
  }
  else{
    var user_q = $('#user_input').val();
    var q = Math.floor(number02 / number01);
    var userq = Number(user_q);
    if (userq == q){
      $(".response").append("<p> Congrats! Your answer is correct. </p>");
    }
    else{
      var finalq = q.toString();
      $(".response").append("<p> Sorry. The correct answer is " + finalq + ".</p>");
    }
  }
}
function setup(){
  if (number01 >= number02){
              $(".function").append("<p>" + n01 + "/" + n02 + "= </p>");
  }
  else {
            $(".function").append("<p>" + n02 + "/" + n01 + "= </p>");
  }
  $("#user_input").keydown(function(event) {

      if (event.keyCode == 13) {
        event.preventDefault();
        console.log("Got here 1");
        DivisionEasy();
        }
      return true;});
  }
$(document).ready(setup)
