import json

# create your first dictionary object
person = {'first': 'John', 'last': 'Forson'}
# add additional key pair values to
person['city'] = 'Accra'

# create a car dictionary 
car = {'car type' : 'Toyota', 'model': 'corolla'}
car['model'] = '2019'

# add dictionary to person dictionary (making it nested)
person['car'] = car

# convert to json format
person_json = json.dumps(person)
# print json object
print(person_json)