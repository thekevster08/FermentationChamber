// Any time an element with the class of "tagline" is clicked
$(".tagline").click(function() {
    alert("jQuery works!");
});

$('#interfaceButton').on("click", function() {
      console.log("clicked");
    //   $('#quote').text('b');
    //   $('#author').text('c');
      $.ajax({
           url: '/interface',
           type: 'POST',
           success: function(response){
              console.log(response);
           },
           error: function(error){
               console.log(error);
           }
       });
});