import os
from flask import Flask

app = Flask(__name__)
@app.route('/')
def index():
    """Main Page with instructions"""
    return "To send a message use /USERNAME/MESSAGE"

 @app.route('/<USERNAME>')
def user(username):
    return "Hi " + username


@app.route('/<USERNAME>/<MESSAGE>')
def send_message(username, message):
     return "{0}: {1}".format(username, message)

app.run(host=os.environ.get('IP', '127.0.0.1'),              
    port=int(os.environ.get('PORT', 5000)),
         debug=True)