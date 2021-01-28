phonebook = {}

while True:
    line = input()
    if line.isdigit():
        for _ in range(int(line)):
            name = input()
            if name not in phonebook:
                print(f'Contact {name} does not exist.')
            else:
                print(f'{name} -> {phonebook[name]}')
        break
    else:
        name, number = line.split('-')
        phonebook[name] = number
