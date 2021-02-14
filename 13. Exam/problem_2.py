command_mapper = {
    'up': lambda x: (x[0] - 1, x[1]),
    'down': lambda x: (x[0] + 1, x[1]),
    'left': lambda x: (x[0], x[1] - 1),
    'right': lambda x: (x[0], x[1] + 1)
}

n = int(input())
pos = None
board = []
coins = 0
for i in range(n):
    row = input().split()
    formatted_row = []
    for j in range(len(row)):
        if row[j].isnumeric():
            formatted_row.append(int(row[j]))
        else:
            formatted_row.append(row[j])
            if row[j] == 'P':
                pos = i, j
    board.append(formatted_row)

win_condition = False
path = []
while True:
    command = input()
    if command not in command_mapper:
        continue
    new_pos = command_mapper[command](pos)
    if 0 <= new_pos[0] < n and 0 <= new_pos[1] < n and board[new_pos[0]][new_pos[1]] != 'X':
        pos = new_pos
        coins += board[pos[0]][pos[1]]
        path.append(pos)
    else:
        coins //= 2
        break
    if coins >= 100:
        win_condition = True
        break
if win_condition:
    print(f'You won! You\'ve collected {coins} coins.')
else:
    print(f'Game over! You\'ve collected {coins} coins.')
print('Your path:')
for p in path:
    print(f'[{p[0]}, {p[1]}]')
