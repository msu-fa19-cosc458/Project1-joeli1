#connect genius api
import requests

url =  "https://api.genius.com/search?q=Beyonce"
my_headers = {"Authorization": "Bearer 9Z1vNErMoWax7Ly0N4_lofj35lnP2NOgDVde0C0h8M5HO0sh09sggU0rXwhDFOQU"}
response = requests.get(url, headers=my_headers)
json_body = response.json()
print(json_body["response"]["hits"][0]["type"])

