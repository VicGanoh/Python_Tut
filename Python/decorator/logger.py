def logger(func):
    def wrapper(): 
        print('Logging execution')
        func()
        print('Done logging')
    return wrapper



@logger 
def simple_message(): 
    print('--Simple message')
    
    
simple_message()