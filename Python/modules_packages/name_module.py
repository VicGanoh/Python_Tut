# importing the module get_name
# from module import get_name
import module

first_name = input('Enter your first name: ')
last_name = input('Enter your last name: ')

name = module.get_name(first_name, last_name)
print(name)
