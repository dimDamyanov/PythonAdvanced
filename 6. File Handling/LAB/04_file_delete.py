import os
try:
    os.remove('File Handling Resources/File Delete/my_first_file.txt')
    print('Deleted')
except FileNotFoundError:
    print('File already deleted')