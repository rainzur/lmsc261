import requests
import json

headers = {
    "AIC-User-Agent": "museum-crawler (rzuraski@berklee.edu)",
    "User-Agent": "museum-crawler (rzuraski@berklee.edu)",
} 

params = { 
	'q' : 'cats', 
	'fields' : "title,artist_display,date_display" # no spaces here
}
q = input("what would u like to search? ")
year_min = input("year min ")
year_max = input("year max ")

# retrieve user input for title and year range.
response = requests.get("https://api.artic.edu/api/v1/artworks", params=params, headers=headers)
data = response.json()
def format_and_print(data, min, max): # data param should be a dict
  art_data = data['data']

  for d in ["art_data"]:
    print([data])
    print([min])
    print([max])
		# get values here
