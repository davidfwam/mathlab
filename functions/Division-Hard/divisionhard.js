
var number05 = Math.floor(Math.random() * 1001);
var number06 = Math.floor(Math.random() * 1001);
var n05 = number05.toString();
var n06 = number06.toString();

function DivisionHard(){
if (number05 >= number06){
    var user_qhard = $('#user_input').val();
    var qhard = Math.floor(number05 / number06);
    var userqhard = Number(user_qhard);
    if (userqhard == qhard){
        $(".response").append("<p> Congrats! Your answer is correct. </p>");
    }
    else{
        var finalqhard = qhard.toString();
        $(".response").append("<p> Sorry. The correct answer is " + finalqhard + ".</p>");
    }
  }
else {
  var user_qhard = $('#user_input').val();
  var qhard = Math.floor(number06 / number05);
  var userqhard = Number(user_qhard);
  if (userqhard == qhard){
      $(".response").append("<p> Congrats! Your answer is correct. </p>");
  }
  else{
      var finalqhard = qhard.toString();
      $(".response").append("<p> Sorry. The correct answer is " + finalqhard + ".</p>");

}
}
}
  function setup(){
    if (number05 >= number06){
        $(".function").append("<p>" + n05 + "/" + n06 + "= </p>");
      }
    else {
      $(".function").append("<p>" + n06 + "/" + n05 + "= </p>");
    }
    $("#submit_button").click(DivisionHard);
  }
$(document).ready(setup)
