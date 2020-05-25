import os
from datetime import datetime
from flask import Flask, redirect, render_template, request, session

app = Flask(__name__)
app.secret_key = "randomstring123"
messages = []

def add_messages(username, message):
    """add messages to messages list, npw is for datetime stamp, hours minutes seconds"""
    now = datetime.now().strftime("%H:%M:%S")
    messages.append("({}) {}: {}".format(now, username, message))

def get_all_messages():
    """get all the messages and separate them with a 'br'"""
    return "<br>".join(messages)

@app.route('/', methods = ["GET", "POST"])
def index():
    """Main Page with instructions"""

    if request.method ==  "POST":
        session["username"] = request.form["username"]

        if "username" in session:
            return redirect(session["username"])

    return render_template("index.html")


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