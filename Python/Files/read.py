# read a text file 

stream = open('../MyPy/Python/Files/demo.txt', 'rt')
# is it readable
print('\nIs this readable? ' + str(stream.readable()))
# print('\n' + stream.read())

# read one character
print('\nRead one character: ' + str(stream.read(1)))

# read to the end of line
print('\nRead to the end of line: ' + str(stream.readline()))

# read all lines to the end of the file
print('\nRead all lines to the end of file: ' + str(stream.readlines()))

stream.close()