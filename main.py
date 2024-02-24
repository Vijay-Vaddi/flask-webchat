from flask import Flask, render_template
from flask_socketio import SocketIO, send
from forms import MessageForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'SECRET123'
socketio = SocketIO(app, cors_allowed_origins="*")
# instantiate socketio and bind it to the app. allow cross origin. 

# message is the key word that's going to trigger
@socketio.on('message')
def handle_message(message):
    print(f"Received message: "+message)

    # if the message is not default one, then broadcast to all
    if message!= "User Connected!":
        send(message, broadcast=True) 

@app.route('/')
def index():
    form = MessageForm()

    return render_template('index.html', form=form)

if __name__ == "__main__":
    # to connect it to local area networks
    socketio.run(app, host="localhost", port=5000, debug=True)

