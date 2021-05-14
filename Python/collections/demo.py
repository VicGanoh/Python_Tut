# create an empty dictionary 
victor = {}
# add people to dictionary with key/pair values
victor['first_name'] = 'Victor'
victor['last_name'] = 'James'

susa = {}
susa['first_name'] = 'Susa'
susa['last_name'] = 'Williams'

# create a list and add the key/value pairs to the
people = []
people.append(victor)
people.append(susa)
people.append({
    'first_name': 'Daniel', 'last_name': 'Forson'})

print(people)