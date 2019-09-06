import requests_oauthlib
import requests

twitter_url = "https://api.twitter.com/1.1/search/tweets.json?q=Beyonce"

oauth = requests_oauthlib.OAuth1(
    "1g57GGgJ7CBOPpGooj9MUKYFk", 
    "C9aFUfRIT1Ad0nB9DN4N0Cn0iQ114kXn2t8dM72NGk0ZH1eoiz",
    "325816963-WBa7ftnAd0H6TwJomBjQr3A1fzOd7Ob1PyQFJbAe",
    "fg4SmCQ0oBAc10P4OD7SWo6rx7QdtZxvwkN8zUlTdvjy3"
)

response = requests.get(twitter_url, auth=oauth)
print(response.json())