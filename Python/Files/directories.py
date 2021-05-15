# navigate through directories
from pathlib import Path

# current working directory
cwd = Path.cwd()
print('Current working directory: ' + str(cwd))

# get parent directory
parent_directory = cwd.parent 
print('\nParent directory: ' + str(parent_directory))

# is this a directory
print('\nIs this a directory? ' + str(parent_directory.is_dir()))

# is this a file
print('\nIs this a file: ' + str(parent_directory.is_file()))

# list child directory
print('\n====Directory Contents======')
for child in parent_directory.iterdir():
    if child.is_dir():
        print(child)
    