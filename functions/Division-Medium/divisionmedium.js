
var number03 = Math.floor(Math.random() * 51 + 1);
var number04 = Math.floor(Math.random() * 51 + 1);

var n03 = number03.toString();
var n04 = number04.toString();
function DivisionMedium(){
if(number03 >= number04){
    var user_qmed = $('#user_input').val();
    var qmed = Math.floor(number03 / number04);
    var userqmed = Number(user_qmed);
    if(userqmed == qmed){
        $(".response").append("<p> Congrats! Your answer is correct. </p>");
    }
    else{
        var final = qmed.toString();

      $(".response").append("<p> Sorry. The correct answer is " + final + ".</p>");
    }
}
else{
  var user_qmed = $('#user_input').val();
  var qmed = Math.floor(number04 / number03);
  var userqmed = Number(user_qmed);
  if(userqmed == qmed){
      $(".response").append("<p> Congrats! Your answer is correct. </p>");
  }
  else{
      var finalqmed = qmed.toString();

      $(".response").append("<p> Sorry. The correct answer is " + finalqmed + ".</p>");
}
}
}
function setup(){
  if (number03 >= number04){
              $(".function").append("<p>" + n03 + "/" + n04 + "= </p>");
            }
  else {
            $(".function").append("<p>" + n04 + "/" + n03 + "= </p>");
          }
          $("#submit_button").click(DivisionMedium);
        }
$(document).ready(setup)
