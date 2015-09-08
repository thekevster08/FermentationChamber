// Any time an element with the class of "tagline" is clicked
//[workspace]-c9-[username].c9.io


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
       
       $.getJSON('../Databases/temperatures.json', function(data) {
    	alert("jQuery works!")
        });
});

$('#setSetpointButton').on("click", function() {
      console.log("submit button clicked");
      $.ajax({
           url: '/setSetpoint',
           type: 'POST',
           success: function(response){
              console.log(response);
           },
           error: function(error){
               console.log(error);
           }
       });
});

