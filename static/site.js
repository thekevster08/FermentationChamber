//http://brewbot-c9-thekevster08.c9.io/

var chart

$(document).ready(function(){
    plotChart();
});

function plotChart(){
    $.getJSON('./static/temperatures.json', function (data) {
        // Create the chart
        var val1 = [];
    	var val2 = [];
    	var val3 = [];
    	var val4 = [];
    	var val5 = [];
    	var val6 = [];
    	var val7 = [];
    	var val8 = [];
    	var val9 = [];
    	$.each(data, function(key,value){
    		val1.push([value[0], value[1]]);
    		val2.push([value[0], value[2]]);
    		val3.push([value[0], value[3]]);
    		val4.push([value[0], value[4]]);
    		val5.push([value[0], value[5]]);
    		val6.push([value[0], value[6]]);
    		val7.push([value[0], value[7]]);
    		val8.push([value[0], value[8]]);
    		val9.push([value[0], value[9]]);
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
    	
        // yAxis: {
        //     title: {
        //         text: 'Temperature (°C)'
        //     },
        //     plotLines: [{
        //         value: 0,
        //         width: 1,
        //         color: '#808080'
        //     }]
        // },
        
        yAxis: [{ //primary
            title: {
                text: 'Temperature (°C)'
            },
            plotLines: [{
                value: 0,
                width: 1,
                color: '#808080'
            }]
        },
        {    
            title: {
                text: 'True/False'
            },
            plotLines: [{
                value: 0,
                width: 1,
                color: '#808080'
            }]
        },
        {
            title: {
                text: 'Percent (%)'
            },
            plotLines: [{
                value: 0,
                width: 1,
                color: '#808080'
            }]
        }],

        legend: {
            layout: 'vertical',
            align: 'right',
            verticalAlign: 'middle',
            borderWidth: 0
        },
        
        series: [{
    		name: 'Wort Temp',
    		type: 'spline',
    		yAxis: 0,
    		data: val1,
    		tooltip: {
    		  valueDecimals: 2
    		}
    	}, 
    	{
    		name: 'Chamber Temp',
    		type: 'spline',
    		yAxis: 0,
    		data: val2,
    		tooltip: {
    		  valueDecimals: 2
    		}
    	}, 
    	{
    		name: 'Ambient Temp',
    		type: 'spline',
    		yAxis: 0,
    		data: val3,
    		tooltip: {
    	      valueDecimals: 2
    		}
    	},
    	{
    		name: 'Primary Setpoint',
    		type: 'line',
    		step: 'left',
    		yAxis: 0,
    		data: val4,
    		tooltip: {
    	      valueDecimals: 2
    		}
    	},
    	{
    		name: 'Secondary Setpoint',
    		yAxis: 0,
    		type: 'spline',
    		data: val5,
    		tooltip: {
    	      valueDecimals: 2
    		}
    	},
    	{
    		name: 'Primary Output',
    		type: 'spline',
    		yAxis: 2,
    		data: val6,
    		tooltip: {
    	      valueDecimals: 2
    		}
    	},
    	{
    		name: 'Secondary Output',
    		yAxis: 2,
    		type: 'spline',
    		data: val7,
    		tooltip: {
    	      valueDecimals: 2
    		}
    	},
    	{
    		name: 'Cold On',
    		type: 'line',
    		step: 'left',
    		yAxis: 1,
    		data: val8,
    		tooltip: {
    	      valueDecimals: 2
    		}
    	},
    	{
    		name: 'Hot Output',
    		yAxis: 1,
    		type: 'line',
    		step: 'left',
    		data: val9,
    		tooltip: {
    	      valueDecimals: 2
    		}
    	}]
        });
            chart = $('#container').highcharts(),        
            // var chart = $('#container').highcharts(),
    $button1 = $('#val1Button');
    $button2 = $('#val2Button');
    $button3 = $('#val3Button');
    $button4 = $('#val4Button');
    $button5 = $('#val5Button');
    $button6 = $('#val6Button');
    $button7 = $('#val7Button');
    $button8 = $('#val8Button');
    $click1 = $('#val1Checkbox');
    
    var x = document.getElementById("myCheck")
    
    
// document.getElementById("myBtn")

// $click1.onclick = function() {
//     // access properties using this keyword
//     console.log("asdf")
//     var series = chart.series[0];
//     if ( series.visible ) {
//         // if checked ...
        
//         series.hide();
//     } else {
//         // if not checked ...
//         series.show();
//     }
// };

// $button1.click(function () {
//     var series = chart.series[0];
//     if (series.visible) {
//         series.hide();
//         $button1.html('Show series');
//     } else {
//         series.show();
//         $button1.html('Hide series');
//     }
// });

// $button2.click(function () {
//     var series = chart.series[1];
//     if (series.visible) {
//         series.hide();
//         $button2.html('Show series');
//     } else {
//         series.show();
//         $button2.html('Hide series');
//     }
// });

// $button3.click(function () {
//     var series = chart.series[2];
//     if (series.visible) {
//         series.hide();
//         $button3.html('Show series');
//     } else {
//         series.show();
//         $button3.html('Hide series');
//     }
// });

// $button4.click(function () {
//     console.log("asdf")
//     var series = chart.series[3];
//     if (series.visible) {
//         series.hide();
//         $button4.html('Show series');
//     } else {
//         series.show();
//         $button4.html('Hide series');
//     }
// });

// $('#val5Button').click(function () {
//     console.log("asdf")
//     var series = chart.series[4];
//     if (series.visible) {
//         series.hide();
//         $button5.html('Show series');
//     } else {
//         series.show();
//         $button5.html('Hide series');
//     }
// });

// $button6.click(function () {
//     var series = chart.series[5];
//     if (series.visible) {
//         series.hide();
//         $button6.html('Show series');
//     } else {
//         series.show();
//         $button6.html('Hide series');
//     }
// });

// $button7.click(function () {
//     var series = chart.series[6];
//     if (series.visible) {
//         series.hide();
//         $button7.html('Show series');
//     } else {
//         series.show();
//         $button7.html('Hide series');
//     }
// });

// $button8.click(function () {
//     var series = chart.series[7];
//     if (series.visible) {
//         series.hide();
//         $button8.html('Show series');
//     } else {
//         series.show();
//         $button8.html('Hide series');
//     }
// });

    });
    

}


// $(function () {<!--from   w w  w.java2s.  com-->
//     $('#container').highcharts({

//         series: [{
//             data: [20, 200, 100, 0.1, 150, 50, 30, 40, 30]
//         }, {
//             data: [20, 200, 100, 0.1, 150, 50, 30, 40, 30].reverse()
//         }]
//     });


//     // the button action
//     var chart = $('#container').highcharts(),
//         $button = $('#button');
//     $button.click(function () {
//         var series = chart.series[0];
//         if (series.visible) {
//             series.hide();
//             $button.html('Show series');
//         } else {
//             series.show();
//             $button.html('Hide series');
//         }
//     });
// });

function val0Click(cb) {
  console.log("Clicked, new value = " + cb.checked);
  var series = chart.series[0];
    if (series.visible) {
        series.hide();
    } else {
        series.show();
    }
}

function val1Click(cb) {
  console.log("Clicked, new value = " + cb.checked);
  var series = chart.series[1];
    if (series.visible) {
        series.hide();
    } else {
        series.show();
    }
}

function val2Click(cb) {
  console.log("Clicked, new value = " + cb.checked);
  var series = chart.series[2];
    if (series.visible) {
        series.hide();
    } else {
        series.show();
    }
}

function val3Click(cb) {
  console.log("Clicked, new value = " + cb.checked);
  var series = chart.series[3];
    if (series.visible) {
        series.hide();
    } else {
        series.show();
    }
}

function val4Click(cb) {
  console.log("Clicked, new value = " + cb.checked);
  var series = chart.series[4];
    if (series.visible) {
        series.hide();
    } else {
        series.show();
    }
}

function val5Click(cb) {
  console.log("Clicked, new value = " + cb.checked);
  var series = chart.series[5];
    if (series.visible) {
        series.hide();
    } else {
        series.show();
    }
}

function val6Click(cb) {
  console.log("Clicked, new value = " + cb.checked);
  var series = chart.series[6];
    if (series.visible) {
        series.hide();
    } else {
        series.show();
    }
}
    
function val7Click(cb) {
  console.log("Clicked, new value = " + cb.checked);
  var series = chart.series[7];
    if (series.visible) {
        series.hide();
    } else {
        series.show();
    }
}

function val8Click(cb) {
  console.log("Clicked, new value = " + cb.checked);
  var series = chart.series[8];
    if (series.visible) {
        series.hide();
    } else {
        series.show();
    }
}

// function val9Click(cb) {
//   console.log("Clicked, new value = " + cb.checked);
//   var series = chart.series[9];
//     if (series.visible) {
//         series.hide();
//     } else {
//         series.show();
//     }
// }

$('#clearButton').on("click", function() {
      console.log("clicked");
      $.ajax({
          url: '/clear',
          type: 'POST',
          success: function(response){
              console.log(response);
          },
          error: function(error){
              console.log(error);
          }
      });
});

$('#startCollectionButton').on("click", function() {
      console.log("start collection clicked");
      $.ajax({
          url: '/startCollection',
          type: 'POST',
          success: function(response){
              console.log(response);
          },
          error: function(error){
              console.log(error);
          }
      });
});

$('#stopCollectionButton').on("click", function() {
      console.log("stop collection clicked");
      $.ajax({
          url: '/stopCollection',
          type: 'POST',
          success: function(response){
              console.log(response);
          },
          error: function(error){
              console.log(error);
          }
      });
});

$('#startControlButton').on("click", function() {
      console.log("start controlclicked");
      $.ajax({
          url: '/startControl',
          type: 'POST',
          success: function(response){
              console.log(response);
          },
          error: function(error){
              console.log(error);
          }
      });
});

$('#stopControlButton').on("click", function() {
      console.log("clicked");
      $.ajax({
          url: '/stopControl',
          type: 'POST',
          success: function(response){
              console.log(response);
          },
          error: function(error){
              console.log(error);
          }
      });
});

$('#coolOnButton').on("click", function() {
      console.log("cool on clicked");
      $.ajax({
          url: '/coolOn',
          type: 'POST',
          success: function(response){
              console.log(response);
          },
          error: function(error){
              console.log(error);
          }
      });
});

$('#coolOffButton').on("click", function() {
      console.log("cool off clicked");
      $.ajax({
          url: '/coolOff',
          type: 'POST',
          success: function(response){
              console.log(response);
          },
          error: function(error){
              console.log(error);
          }
      });
});

$('#heatOnButton').on("click", function() {
      console.log("heat on clicked");
      $.ajax({
          url: '/heatOn',
          type: 'POST',
          success: function(response){
              console.log(response);
          },
          error: function(error){
              console.log(error);
          }
      });
});

$('#heatOffButton').on("click", function() {
      console.log("heat off clicked");
      $.ajax({
          url: '/heatOff',
          type: 'POST',
          success: function(response){
              console.log(response);
          },
          error: function(error){
              console.log(error);
          }
      });
});

$("#saveBtn").click(function() {
     $.ajax({
        type: "GET",
        url: "/save/",
        contentType: "application/json; charset=utf-8",
        data: { saveFilename: $('input[name="saveFilename"]').val() },
        success: function(data) {
            $('#echoResult').text("saved " + data.value);
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
            $('#echoResult').text(data.value + " loaded!");
        }
    });     
});

$("#updateSampleTimeBtn").click(function() {
     $.ajax({
        type: "GET",
        url: "/updateSampleTime",
        contentType: "application/json; charset=utf-8",
        data: { sampleTime: $('input[name="sampleTime"]').val() },
        success: function(data) {
            $('#echoResult').text("updated " + data.value);
        }
    });     
});

$("#updateSetpointButton").click(function() {
     $.ajax({
        type: "GET",
        url: "/updateSetpoint",
        contentType: "application/json; charset=utf-8",
        data: { setpoint: $('input[name="setpoint"]').val() },
        success: function(data) {
            $('#echoResult').text("updated " + data.value);
        }
    });     
});

$("#updateActiveDeadbandButton").click(function() {
     $.ajax({
        type: "GET",
        url: "/updateActiveDeadband",
        contentType: "application/json; charset=utf-8",
        data: { activeDeadband: $('input[name="activeDeadband"]').val() },
        success: function(data) {
            $('#echoResult').text("updated " + data.value);
        }
    });     
});

$("#updateInactiveDeadbandButton").click(function() {
     $.ajax({
        type: "GET",
        url: "/updateInactiveDeadband",
        contentType: "application/json; charset=utf-8",
        data: { inactiveDeadband: $('input[name="inactiveDeadband"]').val() },
        success: function(data) {
            $('#echoResult').text("updated " + data.value);
        }
    });     
});