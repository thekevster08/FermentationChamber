//http://brewbot-c9-thekevster08.c9.io/

$(document).ready(function(){
    plotChart();
});

function plotChart(){
    $.getJSON('/static/temperatures.json', function (data) {
        // Create the chart
        var val1 = [];
    	var val2 = [];
    	var val3 = [];
    	$.each(data, function(key,value){
    		val1.push([value[0], value[1]]);
    		val2.push([value[0], value[2]]);
    		val3.push([value[0], value[3]]);
    	});
    	
        $('#container').highcharts('StockChart', {
            chart: {
            renderTo: 'container',
        },
        
        rangeSelector: {
            enabled: true,
            selected: 2,
        },
        
        title: {
            text: 'Fermentation Temperature',
            x: -20 //center
        },
        
    	xAxis: {
    		type: 'datetime',
    		dateTimeLabelFormats: {
    			second: '%Y-%m-%d'
    		}
    	},
    	
        yAxis: {
            title: {
                text: 'Temperature (°C)'
            },
            plotLines: [{
                value: 0,
                width: 1,
                color: '#808080'
            }]
        },

        legend: {
            layout: 'vertical',
            align: 'right',
            verticalAlign: 'middle',
            borderWidth: 0
        },
        
        series: [{
    		name: 'val1',
    		type: 'spline',
    		data: val1,
    		tooltip: {
    		  valueDecimals: 2
    		}
    	}, 
    	{
    		name: 'val2',
    		type: 'spline',
    		data: val2,
    		tooltip: {
    		  valueDecimals: 2
    		}
    	}, 
    	{
    		name: 'val3',
    		type: 'spline',
    		data: val3,
    		tooltip: {
    	      valueDecimals: 2
    		}
    	}]
        });
    });
}

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

$('#newButton').on("click", function() {
      console.log("clicked");
    //   $('#quote').text('b');
    //   $('#author').text('c');
      $.ajax({
          url: '/new',
          type: 'POST',
          success: function(response){
              console.log(response);
              plotChart();
          },
          error: function(error){
              console.log(error);
          }
      });
       
    //   $.getJSON('../Databases/temperatures.json', function(data) {
    // 	alert("jQuery works!")
    //     });
});

// $('#startCollectionButton').on("click", function() {
//       console.log("clicked");
//     //   $('#quote').text('b');
//     //   $('#author').text('c');
//       $.ajax({
//           url: '/startCollection',
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

// $('#stopCollectionButton').on("click", function() {
//       console.log("clicked");
//     //   $('#quote').text('b');
//     //   $('#author').text('c');
//       $.ajax({
//           url: '/stopCollection',
//           type: 'POST',
//           success: function(response){
//               console.log(response);
//               plotChart();
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

$("#loadBtn").click(function() {
     $.ajax({
        type: "GET",
        url: "/load/",
        contentType: "application/json; charset=utf-8",
        data: { loadFilename: $('input[name="loadFilename"]').val() },
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

