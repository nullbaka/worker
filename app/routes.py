from app import app, socketio

from flask import (
    request,
    render_template,
    session,
    redirect,
)
from flask_socketio import (
    emit,
    disconnect
)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')

    return redirect(url_for('index'))

@socketio.on('connect')
def events_connect():
    print()
    print("------------here-----------")
    print()