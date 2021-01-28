END_COMMAND = 'END'
ADD_COMMAND = 'Add'
SUBTRACT_COMMAND = 'Subtract'

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
while True:
    command = input()
    if command == END_COMMAND:
        break
    else:
        args = command.split()
        row = int(args[1])
        col = int(args[2])
        value = int(args[3])
        if 0 <= row < n and 0 <= col < n:
            if args[0] == ADD_COMMAND:
                matrix[row][col] += value
            elif args[0] == SUBTRACT_COMMAND:
                matrix[row][col] -= value
        else:
            print('Invalid coordinates')

for row in matrix:
    print(' '.join(str(num) for num in row))
