import json

# create dictionary object
person = {'first' : 'John', 'last' : 'Forson'}
# add additional key pair values
person['city'] = 'Ghana'

# create a list 
languages = ['Python', 'Java', 'Javascript']
# add list to dictionary object
person['programming languages'] = languages

# create a json object
person_details_json = json.dumps(person)

# print the json object
print(person_details_json)
