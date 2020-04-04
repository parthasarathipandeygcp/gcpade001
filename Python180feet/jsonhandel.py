import json

#Load a json string in python dict
person = '{"name": "Bob", "languages": ["English", "Fench"]}'
person_dict = json.loads(person)

# Output: {'name': 'Bob', 'languages': ['English', 'Fench']}
print( person_dict)

# Output: ['English', 'French']
print(person_dict['languages'])

#parse a json this file:
projectpath='c:/Users/822024/myproject/gcpade001/'
myfile=projectpath+"data/IndianStates.json"

with open(myfile) as f:
  data = json.load(f)
print(data)
print(data['WB'])


# Convert dict to JSON and write into a file

country_dict={"HN":"Honduras","HK":"Hong Kong","HU":"Hungary","IS":"Iceland","IN":"India"}
country_json = json.dumps(country_dict)

print(country_json)

#Writing JSON to a file
with open(projectpath+'data/country.json', 'w') as json_file:
  json.dump(country_dict, json_file)
