from datetime import datetime

# first_name = 'Victor'
# print('Task completed')
# print(datetime.now())

# for x in range(0,10): 
#     print(x)
# print('Task completed')
# print(datetime.now())

# the above code can be done in a readable and simple way
# with functions

# function to print current date and time
def print_time(task_name):
    print(task_name)
    print(datetime.now())
    
    

first_name = 'Victor'
# call the print_time method
print_time('Task completed successfully')

for x in range(0,10): 
    print(x)
print_time('Loop completed successfully')