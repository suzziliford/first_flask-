from flask import Flask
 
app = Flask(__name__)

@app.route('/')
def hellp_world():
    return "Hello World!"

  