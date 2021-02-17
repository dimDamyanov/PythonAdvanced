from fibonacci_sequence.fibonacci_sequence import create_sequence, locate

while True:
    command = input()
    if command == 'Stop':
        break
    else:
        tokens = command.split()
        if command.startswith('Create'):
            seq = create_sequence(int(tokens[2]))
            print(*seq, sep=' ')
        elif command.startswith('Locate'):
            if result := locate(int(tokens[1])):
                print(f'The number - {tokens[1]} is at index {result}')
            else:
                print(f'The number {tokens[1]} is not in the sequence')
        else:
            exit()
