from flask import Flask
app = Flask(__name__)
@app.route('/')  # Default route . This is the root path through which we access the first page (https://facebook.com is root path)
def hello():
    return 'Hey this is my first Flask app!'

@app.route('/route2') # this is the second path through which we access 2nd page(https://facebook.com/aboutus is sub path)
def adder():
    return "I am on the second page!"

@app.route('/route2/page')
def page():
    return "I am on the third page!"