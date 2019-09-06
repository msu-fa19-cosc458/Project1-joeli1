import flask
import os
import requests
import random
import requests_oauthlib

app = flask.Flask(__name__)

@app.route('/') 
def index(): 
    ##twitter api...hopefully
    twitter_url = "https://api.twitter.com/1.1/search/tweets.json?q=Beyonce"
    random_tweet = random.randint(0,14)
    oauth = requests_oauthlib.OAuth1(
        "1g57GGgJ7CBOPpGooj9MUKYFk", 
        "C9aFUfRIT1Ad0nB9DN4N0Cn0iQ114kXn2t8dM72NGk0ZH1eoiz",
        "325816963-WBa7ftnAd0H6TwJomBjQr3A1fzOd7Ob1PyQFJbAe",
        "fg4SmCQ0oBAc10P4OD7SWo6rx7QdtZxvwkN8zUlTdvjy3"
    )
    response = requests.get(twitter_url, auth=oauth)
    json_body = response.json()
    tweets_about_beyonce = json_body['statuses'][random_tweet]['text']
    
    
    
    #Set Up Genius
    #basic information
    genius_url = "https://api.genius.com/search?q=Beyonce"
    my_headers = {"Authorization": "Bearer 9Z1vNErMoWax7Ly0N4_lofj35lnP2NOgDVde0C0h8M5HO0sh09sggU0rXwhDFOQU"}
        
    playlist = random.randint(0,8)
    response = requests.get(genius_url, headers=my_headers)
    json_body = response.json()
    song = json_body["response"]["hits"][playlist]["result"]["full_title"]
    pic = json_body["response"]["hits"][playlist]["result"]['header_image_url']
    artist = json_body["response"]["hits"][playlist]["result"]['primary_artist']['name']
    return flask.render_template("index.html", song = song, pic= pic, artist = artist, tweets_about_beyonce= tweets_about_beyonce)
    
app.run(port=int(os.getenv('PORT', 8080)), host=os.getenv('IP', '0.0.0.0'))