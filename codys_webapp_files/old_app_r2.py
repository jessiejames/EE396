#!/usr/bin/env python
from flask import Flask, render_template
from flask.ext.socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

# This is where the webpage is formed
@app.route('/')
def index():
	#return 'Hello World!'
	# chedit: change to pull data from the html rather than adding it all here
	return render_template('index.html')

# Display typed message
@socketio.on('my event',namespace='/test')
def test_message(message):
	emit('my response', {'data': message['data']})

# Broadcast the message if broadcast setting is 'True'
@socketio.on('my broadcast event', namespace='/test')
def test_message(message):
	emit('my response', {'data': message['data]}, broadcast=True)

@socketio.on('connect', namespace='/test')
def test_connect():
	emit('my response', {data: Connected'})

@socketio.on('disconnect', namespace='/test')
def test_disconnect():
	print('Client disconnected')

if __name__ == '__main__':
	# host = 0.0.0.0 will be open to any device on the network
	# app.run(debug=True, host='0.0.0.0')
	socketio.run(app)



