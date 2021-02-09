def find_player(matrix):
    matrix_len = len(matrix)
    for i in range(matrix_len):
        for j in range(matrix_len):
            if field[i][j] == 'P':
                return i, j


command_mapper = {
    'up': lambda x: (x[0] - 1, x[1]),
    'down': lambda x: (x[0] + 1, x[1]),
    'right': lambda x: (x[0], x[1] + 1),
    'left': lambda x: (x[0], x[1] - 1),
}
initial_string = input()
n = int(input())
field = []
for _ in range(n):
    row = [ch for ch in input()]
    field.append(row)
m = int(input())
commands = []
for _ in range(m):
    commands.append(input())
pos = find_player(field)

for command in commands:
    new_pos = command_mapper[command](pos)
    if 0 <= new_pos[0] < len(field) and 0 <= new_pos[1] < len(field):
        field[pos[0]][pos[1]] = '-'
        pos = new_pos
        if field[pos[0]][pos[1]] != '-':
            initial_string += field[pos[0]][pos[1]]
        field[pos[0]][pos[1]] = 'P'
    else:
        initial_string = initial_string[:-1]

print(initial_string)
for row in field:
    print(*row, sep='')
