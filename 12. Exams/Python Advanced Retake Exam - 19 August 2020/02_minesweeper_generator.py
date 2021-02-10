def calculate_number(matrix, row, col):
    num = 0
    positions = [
        lambda x: (x[0] + 1, x[1]),
        lambda x: (x[0] - 1, x[1]),
        lambda x: (x[0], x[1] + 1),
        lambda x: (x[0], x[1] - 1),
        lambda x: (x[0] + 1, x[1] + 1),
        lambda x: (x[0] + 1, x[1] - 1),
        lambda x: (x[0] - 1, x[1] + 1),
        lambda x: (x[0] - 1, x[1] - 1)
    ]
    for p in positions:
        new_r, new_c = p((row, col))
        if 0 <= new_r < len(matrix) and 0 <= new_c < len(matrix) and field[new_r][new_c] == '*':
            num += 1
    return num


n = int(input())
field = [['' for _ in range(n)] for _ in range(n)]
bombs_count = int(input())
bombs = []
for _ in range(bombs_count):
    line = input()[1:-1]
    r, c = map(int, line.split(', '))
    field[r][c] = '*'
    bombs.append((r, c))

for r in range(n):
    for c in range(n):
        if field[r][c] != '*':
            field[r][c] = str(calculate_number(field, r, c))

for r in field:
    print(*r, sep=' ')
