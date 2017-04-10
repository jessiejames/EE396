//Code only runs when jQuery detects the document is ready
$(document).ready(function(){
    console.log("app.js: Document is ready")
    //connect to the socket server.
    var socket = io.connect('http://' + document.domain + ':' + location.port + '/test');
    var numbers_received = [];
    console.log("app.js: Connected to socket")    

    //receive details from server
    socket.on('bg_emit', function(msg) {
        //console.log("Received number" + msg.number);
	console.log("app.js: Received bg: " +msg);
 
	//Note: commented out below since not receiving numbers anymore        
	/*
	//maintain a list of ten numbers
        if (numbers_received.length >= 10){
            numbers_received.shift()
        }            
        numbers_received.push(msg.number);
        numbers_string = '';
        for (var i = 0; i < numbers_received.length; i++){
            numbers_string = numbers_string + '<p>' + numbers_received[i].toString() + '</p>';
        }
	*/

        $('#log').html(msg);
    });

});
