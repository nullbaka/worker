from flask import Flask
from flask_socketio import SocketIO

app = Flask(__name__)
app.debug = True
socketio = SocketIO(app, engineio_logger=True)

from app import routes

if __name__ == '__main__':
    socketio.run(app)
