// Any time an element with the class of "tagline" is clicked
//[workspace]-c9-[username].c9.io
//http://brewbot-c9-thekevster08.c9.io/

// $(document).ready(function(){
//     console.log("asdaf");
//     // $.ajax({
//     //     url: 'getData',
//     //     type: 'GET',
//     //     success: function(response){
//     //         alert(response);
//     //     },
//     //     error: function(error){
//     //         alert(error);
//     //     }
//     // })
// });

// $('#startButton').on("click", function() {
//       console.log("clicked");
//     //   $('#quote').text('b');
//     //   $('#author').text('c');
//       $.ajax({
//           url: '/start',
//           type: 'POST',
//           success: function(response){
//               console.log(response);
//           },
//           error: function(error){
//               console.log(error);
//           }
//       });
       
//     //   $.getJSON('../Databases/temperatures.json', function(data) {
//     // 	alert("jQuery works!")
//     //     });
// });

// $('#saveButton').on("click", function() {
//       console.log("save button clicked");
//     //   $('#quote').text('b');
//     //   $('#author').text('c');
//       $.ajax({
//           url: '/start',
//           type: 'POST',
//           success: function(response){
//               console.log(response);
//           },
//           error: function(error){
//               console.log(error);
//           }
//       });
       
//     //   $.getJSON('../Databases/temperatures.json', function(data) {
//     // 	alert("jQuery works!")
//     //     });
// });

$('#openFileInput').on('click', function() {
    $('#openFileInput').trigger('click');
});

$("#saveBtn").click(function() {
     $.ajax({
        type: "GET",
        url: "/save/",
        contentType: "application/json; charset=utf-8",
        data: { saveFilename: $('input[name="saveFilename"]').val() },
        success: function(data) {
            $('#echoResult').text(data.value);
        }
    });     
});


// $(".tagline").click(function() {
//     alert("jQuery works!");
// });

// $('#interfaceButton').on("click", function() {
//       console.log("clicked");
//     //   $('#quote').text('b');
//     //   $('#author').text('c');
//       $.ajax({
//           url: '/interface',
//           type: 'POST',
//           success: function(response){
//               console.log(response);
//           },
//           error: function(error){
//               console.log(error);
//           }
//       });
       
//       $.getJSON('../Databases/temperatures.json', function(data) {
//     	alert("jQuery works!")
//         });
// });

// $('#setSetpointButton').on("click", function() {
//       console.log("submit button clicked");
//       $.ajax({
//           url: '/setSetpoint',
//           type: 'POST',
//           success: function(response){
//               console.log(response);
//           },
//           error: function(error){
//               console.log(error);
//           }
//       });
// });

