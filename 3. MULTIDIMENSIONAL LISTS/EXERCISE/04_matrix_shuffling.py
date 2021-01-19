END_COMMAND = 'END'


def print_matrix(main_matrix):
    for i in range(len(main_matrix)):
        for j in range(len(main_matrix[i])):
            print(main_matrix[i][j], end=' ')
        print()


rows, cols = map(int, input().split())
matrix = [input().split() for _ in range(rows)]
while True:
    is_invalid = False
    command = input()
    if command == END_COMMAND:
        break
    elif command.startswith('swap'):
        arguments = command.split()
        if len(arguments) == 5:
            row1, col1, row2, col2 = map(int, arguments[1:])
            if 0 <= row1 < rows and 0 <= row2 < rows and 0 <= col1 < cols and 0 <= col2 < cols:
                temp = matrix[row1][col1]
                matrix[row1][col1] = matrix[row2][col2]
                matrix[row2][col2] = temp
                print_matrix(matrix)
            else:
                is_invalid = True
        else:
            is_invalid = True
    else:
        is_invalid = True
    if is_invalid:
        print('Invalid input!')
