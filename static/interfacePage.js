$(document).ready(function() {
  // $('.text-primary').text('Hi CodePen!');
  $('#quote').text('-');
  $('#author').text('-');
});

$('#readyButton').on("click", function() {
      $('#quote').text('b');
      $('#author').text('c');
      $.ajax({
          url: '/signUp',
          type: 'POST',
          success: function(response){
              $('#author').text(response);
          }
      })
});