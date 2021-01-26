from collections import deque


def execute(matrix: list, position: tuple,  command: str):
    global coal
    mapper = {
        'left': lambda x: (x[0], x[1] - 1),
        'right': lambda x: (x[0], x[1] + 1),
        'up': lambda x: (x[0] - 1, x[1]),
        'down': lambda x: (x[0] + 1, x[1])
    }
    new_pos = mapper[command](position)
    if 0 <= new_pos[0] < len(matrix) and 0 <= new_pos[1] < len(matrix):
        if matrix[new_pos[0]][new_pos[1]] == 'c':
            matrix[new_pos[0]][new_pos[1]] = '*'
            coal -= 1
        return new_pos
    return position


n = int(input())
commands = deque(input().split())
grid = [input().split() for _ in range(n)]
pos = 0, 0
coal = 0
flag = False
for i in range(n):
    for j in range(n):
        if grid[i][j] == 's':
            pos = i, j
        elif grid[i][j] == 'c':
            coal += 1

current_pos = pos
while commands:
    current_command = commands.popleft()
    current_pos = execute(grid, pos, current_command)
    if grid[current_pos[0]][current_pos[1]] == 'e':
        print(f'Game over! ({current_pos[0]}, {current_pos[1]})')
        flag = True
    elif coal == 0:
        print(f'You collected all coals! ({current_pos[0]}, {current_pos[1]})')
        flag = True
    pos = current_pos
if not flag:
    print(f'{coal} coals left. ({current_pos[0]}, {current_pos[1]})')
