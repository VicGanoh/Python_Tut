# this tutorial is on the various ways were strings can be formated using the
# the .format()

first_name = input('Please enter your first name: ')
last_name = input('Please enter your last name: ')
# output = 'Hello, ' + first_name + ' ' + last_name 

# print(output)

# over here we introduce the format with placeholder to make our code simple
# output = 'Hello, {}, {}'.format(first_name, last_name)
# print(output)

# output = 'Hello, {1}, {0}'.format(first_name, last_name)
# print(output)

# this supports python 3 above
output = f'Hello, {first_name} {last_name}'
print(output)