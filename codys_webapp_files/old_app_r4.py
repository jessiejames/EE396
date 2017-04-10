#!/usr/bin/env python
from flask import Flask, render_template, session, request
from flask_socketio import SocketIO, emit, join_room, leave_room, \
    close_room, rooms, disconnect

# Set this variable to "threading", "eventlet" or "gevent" to test the
# different async modes, or leave it set to None for the application to choose
# the best option based on installed packages.
async_mode = None

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
# chedit: turn on debugging
app.debug = True

socketio = SocketIO(app, async_mode=async_mode)
thread = None

@app.route('/template', methods=['GET', 'POST'])
def template():
	if request.method == 'POST':
		return "Hello"
	return render_template('index.html', async_mode=socketio.async_mode)

if __name__ == '__main__':
    socketio.run(app, debug=True, host='0.0.0.0')
    # chedit: added the host='0.0.0.0' above

