# A student makes honour roll if average is >=85
# adn their lowest grade is not below 70
gpa = float(input('What was your GPA(Grade Average Point): '))

lowest_grade = float(input('What was your lowest grade? '))

# if gpa >= .85 and lowest_grade >= .70: 
#     print('Congrats! You made the honour roll.')
# else:
#     print('Sorry you could not make the honour roll')

if gpa >= .85 and lowest_grade >= .70: 
    honour_roll = True
else:
    honour_roll = False
    
if honour_roll: 
    print('Congrats! You made the honour roll.')
else: 
    print('Sorry you could not make the honour roll')