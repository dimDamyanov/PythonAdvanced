command_mapper = {
    'up': lambda x: (x[0] - 1, x[1]),
    'down': lambda x: (x[0] + 1, x[1]),
    'right': lambda x: (x[0], x[1] + 1),
    'left': lambda x: (x[0], x[1] - 1),
}

n = int(input())
snake_pos = None
burrow_pos = None
field = []
food_quantity = 0
for i in range(n):
    line = input()
    row = []
    for j in range(n):
        if line[j] == 'S':
            snake_pos = i, j
        elif line[j] == 'B':
            if not burrow_pos:
                burrow_pos = []
            burrow_pos.append((i, j))
        row.append(line[j])
    field.append(row)

winning_flag = False
while True:
    command = input()
    new_r, new_c = command_mapper[command](snake_pos)
    if 0 <= new_r < len(field) and 0 <= new_c < len(field):
        field[snake_pos[0]][snake_pos[1]] = '.'
        snake_pos = new_r, new_c
        if field[snake_pos[0]][snake_pos[1]] == '*':
            food_quantity += 1
            field[snake_pos[0]][snake_pos[1]] = 'S'
        elif field[snake_pos[0]][snake_pos[1]] == 'B':
            field[snake_pos[0]][snake_pos[1]] = '.'
            for pos in burrow_pos:
                if pos != snake_pos:
                    snake_pos = pos
            burrow_pos.clear()
            field[snake_pos[0]][snake_pos[1]] = 'S'
        else:
            field[snake_pos[0]][snake_pos[1]] = 'S'
    else:
        field[snake_pos[0]][snake_pos[1]] = '.'
        break
    if food_quantity >= 10:
        winning_flag = True
        break
if winning_flag:
    print('You won! You fed the snake.')
else:
    print('Game over!')
print(f'Food eaten: {food_quantity}')
for row in field:
    print(*row, sep='')
