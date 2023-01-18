from flask import Flask, request, redirect, render_template, url_for, Response
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


@app.route('/')
def index():
    return render_template("chat.html")
@socketio.on('message')
def handleMessage(msg):
    send(msg, broadcast = True)

socketio.run(app)

