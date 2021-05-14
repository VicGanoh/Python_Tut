city = input('Which city do you live in: ')
tax = 0

# if city.capitalize() == 'Accra': 
#     tax = 0.05
# elif city.capitalize() == 'Tema': 
#     tax = 0.05
# elif city.capitalize() == 'Kumasi': 
#     tax = 0.05
# else: 
#     tax = 0
# print('Your tax is: ' + str(tax))

# code modification
# if city.capitalize() == 'Accra' or city.capitalize() == 'Tema' or city.capitalize() == 'Kumasi':
#     tax = .05
# else: 
#     tax = 0
# print(tax)

if city.capitalize() in ('Accra','Tema'): 
    tax = 0.05
elif city.capitalize() == 'Sunyani': 
    tax = 0.12
else: 
    tax = 0;   
print(tax)