var numberj = Math.floor(Math.random() * 51);
var numberk = Math.floor(Math.random() * 51);

var nj = (numberj).toString();
var nk = (numberk).toString();
function SubtractionMed(){
if (numberj >= numberk){
    var user_differencemed = $('#user_input').val();
    var differencemed = numberj - numberk;
    var userdifferencemed = Number(user_differencemed);
    if (userdifferencemed == differencemed){
        $(".response").append("<p> Congrats! Your answer is correct. </p>");
      }
    else{
        var finaldifferencemed = differencemed.toString();
        $(".response").append("<p> Sorry. The correct answer is " + finaldifferencemed + ".</p>");
      }
    }
else{
    var user_differencemed = $('#user_input').val();
    var differencemed = numberk - numberj;
    var userdifferencemed = Number(user_differencemed);
    if (userdifferencemed == differencemed){
        $(".response").append("<p> Congrats! Your answer is correct. </p>");
      }
    else{
        finaldifferencemed = differencemed.toString();
        $(".response").append("<p> Sorry. The correct answer is " + finaldifferencemed + ".</p>");
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
          $("#submit_button").click(SubtractionMed);
        }
$(document).ready(setup)
