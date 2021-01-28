def validate_pos(matrix, pos):
    return 0 <= pos[0] < len(matrix) and 0 <= pos[1] < len(matrix[pos[0]])


def print_lair(matrix):
    print(*[''.join(ch for ch in row) for row in matrix], sep='\n')


def find_player(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 'P':
                return i, j


def spread_bunnies(matrix):
    bunnies = set()
    spread_cells = [
        lambda x: (x[0] - 1, x[1]),
        lambda x: (x[0] + 1, x[1]),
        lambda x: (x[0], x[1] - 1),
        lambda x: (x[0], x[1] + 1),
    ]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 'B':
                bunnies.add((i, j))
    for bunny in bunnies:
        for cell in spread_cells:
            pos = cell(bunny)
            if validate_pos(matrix, pos):
                matrix[pos[0]][pos[1]] = 'B'


def execute(matrix, command, pos):
    mapper = {
        'U': lambda x: (x[0] - 1, x[1]),
        'D': lambda x: (x[0] + 1, x[1]),
        'L': lambda x: (x[0], x[1] - 1),
        'R': lambda x: (x[0], x[1] + 1),
    }
    new_pos = mapper[command](pos)
    if not validate_pos(matrix, new_pos):
        matrix[pos[0]][pos[1]] = '.'
        spread_bunnies(matrix)
        print_lair(lair)
        print(f'won: {pos[0]} {pos[1]}')
        return 0
    elif matrix[new_pos[0]][new_pos[1]] == 'B':
        matrix[pos[0]][pos[1]] = '.'
        spread_bunnies(matrix)
        print_lair(lair)
        print(f'dead: {new_pos[0]} {new_pos[1]}')
        return 0
    else:
        matrix[pos[0]][pos[1]] = '.'
        matrix[new_pos[0]][new_pos[1]] = 'P'
        spread_bunnies(matrix)
        if matrix[new_pos[0]][new_pos[1]] == 'B':
            print_lair(lair)
            print(f'dead: {new_pos[0]} {new_pos[1]}')
            return 0


n, m = map(int, input().split())
lair = [[ch for ch in input()] for _ in range(n)]
commands = [ch for ch in input()]
for command in commands:
    player_position = find_player(lair)
    code = execute(lair, command, player_position)
    if code == 0:
        break
