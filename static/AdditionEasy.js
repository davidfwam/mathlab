var numberone = Math.floor(Math.random() * 11);
var numbertwo = Math.floor(Math.random() * 11);
var n1 = numberone.toString();
var n2 = numbertwo.toString();
function AdditionEasy(){
/*var numberone = Math.floor(Math.random() * 11);
var numbertwo = Math.floor(Math.random() * 11);
var n1 = numberone.toString();
var n2 = numbertwo.toString();
$(".function").append("<p>" + n1 + "+" + n2 + "= </p>"); */
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
  $("#submit_button").click(AdditionEasy);


}

 $(document).ready(setup)
