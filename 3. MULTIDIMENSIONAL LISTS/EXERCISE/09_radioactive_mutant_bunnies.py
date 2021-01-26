def execute(matrix: list, position: tuple, command: str):
    mapper = {
        'L': lambda x: (x[0], x[1] - 1),
        'R': lambda x: (x[0], x[1] + 1),
        'U': lambda x: (x[0] - 1, x[1]),
        'D': lambda x: (x[0] + 1, x[1])
    }
    bunnies = [(i, j) for i in range(len(matrix)) for j in range(len(matrix[0])) if matrix[i][j] == 'B']
    for bunny in bunnies:
        for direction in mapper:
            new_bunny = mapper[direction](bunny)
            if 0 <= new_bunny[0] < len(matrix) and 0 <= new_bunny[1] < len(matrix):
                matrix[new_bunny[0]][new_bunny[1]] = 'B'
    new_position = mapper[command](position)
    if
    pass


rows, cols = map(int, input().split())
lair = [[ch for ch in input()] for _ in range(len(rows))]
pos = 0, 0
for i in range(rows):
    for j in range(cols):
        if lair[i][j] == 'P':
            pos = i, j
