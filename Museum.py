headers = {
    "AIC-User-Agent": "museum-crawler (rzuraski@berklee.edu)",
    "User-Agent": "museum-crawler (rzuraski@berklee.edu)",
} 

params = { 
	'q' : 'cats', 
	'fields' : "title,artist_display,date_display" # no spaces here
}

params_q = input("What would u like to search? ")
min = input("What's the minimum year u want to search? ")
max = input("What's the maximum year u want to search? ")
# retrieve user input for title and year range.
response = requests.get("https://api.artic.edu/api/v1/artworks", params=params, headers=headers)
def format_and_print(data, min, max): # data param should be a dict
  art_data = data['data']

  for d in art_data:
    print(result[data])
    print(result[min])
    print(result[max])
		# get values here
