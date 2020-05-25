import os
from flask import Flask

app = Flask(__name__)
messages = []

def add_messages(username, message):
    """add messages to messages list"""
    messages.append("{}: {}".format(username, message)) 

def get_all_messages():
    """get all the messages and separate them with a 'br'"""
    return "<br>".join(messages)

@app.route('/')
def index():
    """Main Page with instructions"""
    return "To send a message use /USERNAME/MESSAGE"


@app.route("/<username>")
def user(username):
    """ display chat messages"""
    return "Welcome {0} - {1}".format(username, get_all_messages())


@app.route("/<username>/<message>")
def send_message(username, message):
    """Create a new message and redirect to chat page"""
    add_messages(username, message)
    return redirect(username)

app.run(host=os.environ.get('IP', '127.0.0.1'),              
    port=int(os.environ.get('PORT', 5000)),
         debug=True)