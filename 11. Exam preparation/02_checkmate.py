directions = [
    lambda x: (x[0] - 1, x[1]),
    lambda x: (x[0] + 1, x[1]),
    lambda x: (x[0], x[1] - 1),
    lambda x: (x[0], x[1] + 1),
    lambda x: (x[0] - 1, x[1] - 1),
    lambda x: (x[0] - 1, x[1] + 1),
    lambda x: (x[0] + 1, x[1] - 1),
    lambda x: (x[0] + 1, x[1] + 1)
]


board = []
king_pos = None
for i in range(8):
    row = input().split()
    board.append(row)
    for j in range(8):
        if row[j] == 'K':
            king_pos = i, j

queens = []
for i in range(len(directions)):
    direction = directions[i]
    new_pos = king_pos
    while True:
        new_pos = direction(new_pos)
        if not (0 <= new_pos[0] < 8 and 0 <= new_pos[1] < 8):
            break
        if board[new_pos[0]][new_pos[1]] == 'Q':
            queens.append(new_pos)
            break
if queens:
    for queen in queens:
        print(f'[{", ".join([str(el) for el in queen])}]')
else:
    print('The king is safe!')
