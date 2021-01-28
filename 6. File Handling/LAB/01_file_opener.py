try:
    with open('../File Handling Resources/File Opener/text.txt') as file:
        print('File found')
except FileNotFoundError:
    print('File not found error')
