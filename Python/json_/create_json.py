import json

# create a dictionary object
person = {'first': 'Michael', 'last' : 'Smith'}
# Add additional key pairs
person['city'] = 'Accra'

# Convert dictionary to JSON object
person_json = json.dumps(person)

# print JSON object
print(person_json)