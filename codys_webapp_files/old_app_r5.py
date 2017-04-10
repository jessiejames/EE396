from flask import Flask, render_template
from flask.ext.socketio import SocketIO, emit
from numpy import genfromtxt
import json

app = Flask(__name__)
socketio=SocketIO(app)

##############################
# Parse in .csv file here
##############################
import csv
#with open('./data/data.csv', 'rb') as csvfile:
#	txtreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
#	i = 1;
#	for row in txtreader:
#		print ', '.join(row)
my_data = genfromtxt('./data/data.csv', delimiter=',')
print (+my_data)
print(+my_data[1])

##############################
# Send Websockets
##############################
@app.route('/')
def index():
	# chedit: pull data from the html rather than adding it all here
	return render_template('index.html')

# "send_message" is the event it will look for
@socketio.on('send_message') 
def handle_source(json_data):
	text = json_data['message'].encode('ascii','ignore')
	#new_text = my_data['message'].encode('ascii','ignore')
	#print("new text is "+new_text)
	#print "test"
	# trigger new event, 'echo2'
	socketio.emit('echo2', {'echo2': 'Server Says: '+text})
	#socketio.emit('echo2', {'echo2': 'Server Says: '+new_text})

# chedit: created below
@ socketio.on('send_extra')
def handle_extra(json_date):
	socketio.emit('echo', {'echo': 'Adding this data'})

# chedit: upon connection, start sending messages
#@socketio.on('connect')
#def test_connect():



if __name__ == '__main__':
	# host = 0.0.0.0 will be open to any device on the network
	#app.run(debug=True, host='0.0.0.0')
	socketio.run(app,debug=True, host='0.0.0.0')



