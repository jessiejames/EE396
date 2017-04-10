from flask import Flask, render_template
from flask.ext.socketio import SocketIO, emit
from numpy import genfromtxt
from random import random
from time import sleep
from threading import Thread, Event
import json

import eventlet
eventlet.monkey_patch()

app = Flask(__name__)
app.config['DEBUG'] = True
# Turn Flask app into a Socketio app
#socketio=SocketIO(app)
#socketio=SocketIO(app, async_mode="eventlet")
socketio=SocketIO(app, logger=True, engineio_logger=True)

@app.route('/')
def index():
    #only by sending this page first will the client be connected to the socketio instance
    return render_template('index.html')

@socketio.on('connect', namespace='/test')
def test_connect():
    # need visibility of the global thread object
    global thread
    print('Client connected')

#chedit: added the below:
def bg_emit():
    socketio.emit('bg_emit', "Testing", namespace='/test')

def listen():
    while True:
	# chedit: possibly change below to a real-time update
	bg_emit()
	eventlet.sleep(5)

# chedit: perform the listen definition upon entering (I believe) 
eventlet.spawn(listen)

@socketio.on('disconnect', namespace='/test')
def test_disconnect():
    print('Client disconnected')


if __name__ == '__main__':
	# host = 0.0.0.0 will be open to any device on the network
	#app.run(debug=True, host='0.0.0.0')
	socketio.run(app,debug=True, host='0.0.0.0')


