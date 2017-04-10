$(document).ready(function(){
    console.log("plot_chart.js: starting now");
    // Note: the following code updates w/ the appropriate timeouts
    var chart = c3.generate({
     data: {
	x: 'x',
	columns: [
	    ['x', 	1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
	    ['data1',   0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
	],
	type: 'spline'
    },
    // Chedit: added the settings below to speed up rendering
    transition: {
    	duration: 0
    },
    interaction: {
	enabled: false
    },
    point: {
	show: false
    },
    
    
    });
 
    var timestamp = 1;
    var x_count = 1;

    //connect to the socket server.
    var socket = io.connect('http://' + document.domain + ':' + location.port + '/test');
    var numbers_received = [];
    console.log("app.js: Connected to socket")    

    //receive details from server
    socket.on('bg_emit', function(msg) {
        //console.log("Received number" + msg.number);
	console.log("app.js: Received bg: " +msg);
	// Update data to the number list
        $('#log').html(msg);
	// Update the websocket here
	timestamp = timestamp + 0.1;
	x_count = x_count + 1;
	console.log("app.js: timestamp and xcount: " +timestamp, +x_count);
	setTimeout(function () {
	     chart.flow({
                 columns: [
                     ["x", x_count],
                     ["data1", msg],
                 ],
               length: 0,
             });
	    // Update axes here to spread out: 
	    //chart.axis.min({x: 1});
	    //chart.axis.max({x: x_count});
        }, timestamp);       

    });

});
