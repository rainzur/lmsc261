import json

data_json = open("ramps.json")
data_dict = json.load(data_json)

ramp_list = data_dict

names = ramp_list.keys

print(names)

