from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/about')
def about():
    return 'about'

@app.route('/volunteer')
def volunteer():
    return 'volunteer'