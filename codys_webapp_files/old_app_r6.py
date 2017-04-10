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
socketio=SocketIO(app, 

# Random Number Generator
thread = Thread()
thread_stop_event = Event()

class RandomThread(Thread):
    def __init__(self):
	self.delay = 1
	super(RandomThread, self).__init__()

    def randomNumberGenerator(self):
        """
        Generate a random number every 1 second and emit to a socketio instance (broadcast)
        Ideally to be run in a separate thread?
        """
        #infinite loop of magical random numbers
        print "Making random numbers"
        while not thread_stop_event.isSet():
            number = round(random()*10, 3)
            print number
            socketio.emit('newnumber', {'number': number}, namespace='/test')
            print "app.py: emitted newnumber"
	    sleep(self.delay)

    def run(self):
        self.randomNumberGenerator()


@app.route('/')
def index():
    #only by sending this page first will the client be connected to the socketio instance
    return render_template('index.html')

@socketio.on('connect', namespace='/test')
def test_connect():
    # need visibility of the global thread object
    global thread

    print('Client connected')

    #Start the random number generator thread only if the thread has not been started before.
    if not thread.isAlive():
        print "Starting Thread"
        thread = RandomThread()
        #chedit: create a daemon thread so it dies when main thread exits
	thread.start()

@socketio.on('disconnect', namespace='/test')
def test_disconnect():
    print('Client disconnected')



if __name__ == '__main__':
	# host = 0.0.0.0 will be open to any device on the network
	#app.run(debug=True, host='0.0.0.0')
	socketio.run(app,debug=True, host='0.0.0.0')



