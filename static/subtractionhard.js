
var numberj = Math.floor(Math.random() * (1001 - 50));
var numberk = Math.floor(Math.random() * (1001 - 50));

var nj = (numberj).toString();
var nk = (numberk).toString();
function SubtractionHard(){
if (numberj >= numberk){
    var user_differencehard = $('#user_input').val();
    var differencehard = numberj - numberk;
    var userdifferencehard = Number(user_differencehard);
    if (userdifferencehard == differencehard){
        $(".response").append("<p> Congrats! Your answer is correct. </p>");
      }
    else{
        var finaldifferencehard = differencehard.toString();
        $(".response").append("<p> Sorry. The correct answer is " + finaldifferencehard + ".</p>");
      }
    }
else{
    var user_differencehard = $('#user_input').val();
    var differencehard = numberk - numberj;
    var userdifferencehard = Number(user_differencehard);
    if (userdifferencehard == differencehard){
        $(".response").append("<p> Congrats! Your answer is correct. </p>");
      }
    else{
        var finaldifferencehard = differencehard.toString();
        $(".response").append("<p> Sorry. The correct answer is " + finaldifferencehard + ".</p>");
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
                SubtractionHard();
                }
              return true;});
        }
$(document).ready(setup)
