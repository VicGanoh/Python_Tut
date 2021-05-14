# Get current date and time we need to use the datetime library
from datetime import datetime, timedelta

# current_date = datetime.now()
# The now function returns current date and time as a datetime object

# You must convert the datetime object to a string 
# before you can concatenate it to another string
# print("Today's date: " + str(current_date))

todays_date = datetime.now()
print('Today is: ' + str(todays_date))
print()

# formating date into day, month and year as
print('Todays day: ' + str(todays_date.day))
print('Todays month: ' + str(todays_date.month))
print('Todays year: ' + str(todays_date.year))


print('Hour: ' + str(todays_date.hour))
print('Minute(s): ' + str(todays_date.minute))
print('Second(s): ' + str(todays_date.second))


# Using timedelta to add or remove days, or weeks to a date 
# one_day = timedelta(days=1)
# yesterday_date = todays_date -  one_day
# print("Yesterday's date: " + str(yesterday_date))

# Now i want to know pervious week date 
# one_week= timedelta(weeks=1)
# weeks_date = todays_date - one_week
# print('Previous week date: ' + str(weeks_date))

