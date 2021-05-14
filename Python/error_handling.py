x = 14
y = 0
# this generates an error.
# print(x/y)

# Lets handle the error using the try/except statement.
# try some statements
try:
    print(x/y)
# print type of error
except ZeroDivisionError as e:
    print('Cannot divide by zero.')
else:
    print('Done.')
finally:
    print('Thank You.')    
