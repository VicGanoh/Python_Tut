#  Grab the library
from pathlib import Path

# what is the current working directory
current_directory = Path.cwd()
print('Current working directory: ' + str(current_directory))

# Create full path name by joining path and filename
new_file = Path.joinpath(current_directory, 'new_file.txt')
print('\nFull path:\n' + str(new_file))

# check if file exists
print('Does file exist? ' + str(new_file.exists()))