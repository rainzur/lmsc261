import requests 
import json 

station_codes = {
    'Hynes' : 'place-hymnl',
    'Washington Street' : 'place-wascm',
    'Packards Corner' : 'place-brico',
    'Kenmore' : 'place-kencl',
    'Harvard Avenue' : 'place-harvd'
}

station_key = input("what station are ya at? ")
station_value = station_codes.get(station_key, 'place-hymnl')

queries = {
    'filter[stop]' : station_value,
    'filter[route]' : 'Green-B',
    'page[limit]' : 1
}

def does_station_exist(codes, key):
    for k in codes.keys():
        if (k != key): continue
        else: 
            return True
            break

    return False



if (does_station_exist(station_codes, station_key)):
    response = requests.get("https://api-v3.mbta.com/predictions", params=queries)
    data = response.json()
    time = data['data'][0]['attributes']['departure_time']
    print(f"your train at {station_key} will be at {time}")

else:
    print("station does not exist!!")