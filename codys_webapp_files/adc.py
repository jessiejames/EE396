#######################################################################################
# Simple demo of reading each analog input from the ADS1x15 and printing it to
# the screen. Adding functionality of displaying in c3 or d3 chart
#######################################################################################
from flask import Flask, render_template
from flask.ext.socketio import SocketIO, emit
from numpy import genfromtxt
from time import sleep
import time
from threading import Thread, Event
import json
import eventlet
eventlet.monkey_patch()
# Import the ADS1x15 module.
import Adafruit_ADS1x15
from multiprocessing import Process

app = Flask(__name__)
app.config['DEBUG'] = True
socketio = SocketIO(app, logger=False, engineio_logger=False)

#######################################################################################
# Define socketio functions
#######################################################################################
@app.route('/')
def index():
    print('**ENTER: index()**')
    #This is where the page will be created
    return render_template('adc_index.html')

@socketio.on('connect', namespace='/test')
def test_connect():
    print('**ENTER: test_connect()**')
    #Provide visibility of global thread object
    global thread
    print('Client connected')

def bg_emit(adc_val):
    print('**ENTER: bg_emit()**')
    print('bg_emit(): adc_val is {}'.format(adc_val))
    socketio.emit('bg_emit', adc_val, namespace='/test')   

def listen():
    print('**ENTER: listen()**')
    while True:
	####################
   	# Read ADC values
	####################
	adc = Adafruit_ADS1x15.ADS1115()
	GAIN = 1
	print('Reading ADS1x15 values, press Ctrl-C to quit...')
	print('| {0:>6} | {1:>6} | {2:>6} | {3:>6} |'.format(*range(4)))
	print('-' * 37)
	# Read all the ADC channel values in a list.
	values = [0]*4
	for i in range(4):
	    values[i] = adc.read_adc(i, gain=GAIN)
	    #print('Current value is {}'.format(values[i]))
	print('| {0:>6} | {1:>6} | {2:>6} | {3:>6} |'.format(*values))
	
	# Note: mark-down the timing values below when it is more fine-tuned
	# Pause for half a second.
	time.sleep(0.1)
	bg_emit(values[1])
	eventlet.sleep(0.1)

eventlet.spawn(listen)

@socketio.on('disconnect', namespace='/test')
def test_disconnect():
    print('**ENTER: test_disconnect()**')
    print('Client disconnected')

if __name__ == '__main__':
    socketio.run(app, debug=True, host='0.0.0.0')



