numbers_dictionary = {}


while True:
    line = input()
    if line == 'Search':
        break
    try:
        number_as_string = line
        number = int(input())
        numbers_dictionary[number_as_string] = number
    except ValueError:
        print('The variable must be an integer')

while True:
    line = input()
    if line == 'Remove':
        break
    try:
        searched = line
        print(numbers_dictionary[searched])
    except KeyError:
        print('Number does not exist in dictionary')


while True:
    line = input()
    if line == 'End':
        break
    try:
        searched = line
        numbers_dictionary.pop(searched)
    except KeyError:
        print('Number does not exist in dictionary')

print(numbers_dictionary)
