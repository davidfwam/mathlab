var numberj = Math.floor(Math.random() * 11);
var numberk = Math.floor(Math.random() * 11);

var nj = (numberj).toString();
var nk = (numberk).toString();
function SubtractionMed(){
if (numberj >= numberk){
    var user_difference = $('#user_input').val();
    var difference = numberj - numberk;
    var userdifference = Number(user_difference);
    if (userdifference == difference){
        $(".response").append("<p> Congrats! Your answer is correct. </p>");
      }
    else{
        var finaldifference = difference.toString();
        $(".response").append("<p> Sorry. The correct answer is " + finaldifference + ".</p>");
      }
    }
else{
    var user_difference = $('#user_input').val();
    var difference = numberk - numberj;
    var userdifference = Number(user_difference);
    if (userdifference == difference){
        $(".response").append("<p> Congrats! Your answer is correct. </p>");
      }
    else{
        finaldifference = difference.toString();
        $(".response").append("<p> Sorry. The correct answer is " + finaldifference + ".</p>");
      }
}
}
function setup(){
  if (numberj >= numberk){
              $(".function").append("<p>" + nj + "-" + nk + "= </p>");
            }
  else {
            $(".function").append("<p>" + nk + "-" + nj + "= </p>");
          }
          $("#user_input").keydown(function(event) {

              if (event.keyCode == 13) {
                event.preventDefault();
                console.log("Got here 1");
                SubtractionMed();
                }
              return true;});
        }
$(document).ready(setup)
