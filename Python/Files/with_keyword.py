# using the with command to close a file after working with instead of
# closing the file manually.
# try:       
#     stream = open('file.txt', 'wt')
#     stream.write('A random text')
# finally:
#     stream.close() # closing the file after working with it is really important
    

# alternatively,
with open('file_.txt', 'wt') as stream:
    stream.write('A random text')