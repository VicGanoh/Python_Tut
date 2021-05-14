from datetime import datetime

# ask user for birthday
birth_date = input('Please enter your birthday (dd/mm/yyyy): ')

birth_date = datetime.strptime(birth_date, '%d/%m/%Y')
print('Your birthday: ' + str(birth_date))