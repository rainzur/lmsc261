import requests
import json

queries = {
    "term" : "flume",
    "media" : "musicVideo",
    "entity" : "musicArtist",
    "limit" : 5
}
queries ["term"] = input("what do you want to serach? ")
queries["limit"] = int(input("how many results u want"))
response = requests.get("https://itunes.apple.com/search?", params=queries)
data = response.json()

for result in data ["results"]:
    print(result["artistName"])
    print(result["trackName"])
    print(result["releaseDate"])
    print("---------------")

import requests
import json 

try:
    # do something risky here
    response = requests.get("http://catfact.ninja/fact") #protocol name/domain name/query
    data = response.json()
    formatted = json.dumps(data, indent=4)
    print(data.get("fact", "fact not found")) #this is the way to program defensively. .get is the preferred method

except requests.exceptions.ConnectionError:
    print("pay your internet bills you fking bum")

