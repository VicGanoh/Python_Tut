# Create a file and open for writing
stream = open('file.txt', 'wt')

print('\nCan I write to this file? ' + str(stream.writable()) + '\n')

stream.write('H') # Write a single string
stream.writelines(['ello',' ','world']) # Write one or more stringStart
stream.write('\n') # Write a new line 

