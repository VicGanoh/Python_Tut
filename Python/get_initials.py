# a function to return initials of user 
def get_initials(name):
    initials = name[0:1].upper()
    return initials




# Ask for someones name and return the initials
first_name = input('Enter your first name: ')
# first_name_initial = get_initials(first_name)
last_name = input('Enter your last name: ')
# last_name_initial = get_initials(last_name)

# print('Your initials are: ' + first_name + last_name)
print('Your initials are: ' + get_initials(first_name) + get_initials(last_name))
# initials = f'Your initials are: {first_name}{last_name}'
# print(initials)