import flask
import os
import requests

app = flask.Flask(__name__)

@app.route('/') 
def index(): 
    print("This is a debug statement!")
    return("<b>Hello, world!</b>")
    
app.run(
    port=int(os.getenv('PORT', 8080)),
    host=os.getenv('IP', '0.0.0.0'))


url = "https://api.genius.com/search?q=Beyonce"


response = requests.get(url)
print(response.text)
