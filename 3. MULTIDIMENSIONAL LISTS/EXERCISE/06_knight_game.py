def validate_pos(matrix: list, pos: tuple):
    return 0 <= pos[0] < len(matrix) and 0 <= pos[1] < len(matrix)


def get_vulnerable(matrix: list, r: int, c: int):
    vulnerable = {(r - 2, c + 1), (r - 1, c + 2), (r + 1, c + 2), (r + 2, c + 1), (r + 2, c - 1), (r + 1, c - 2),
                  (r - 1, c - 2), (r - 2, c - 1)}
    return set(pos for pos in vulnerable if validate_pos(matrix, pos) and matrix[pos[0]][pos[1]] == 'K')


n = int(input())
board = [[ch for ch in input()] for _ in range(n)]
knights = {}
for i in range(n):
    for j in range(n):
        if board[i][j] == 'K':
            knights[i, j] = get_vulnerable(board, i, j)
knights = {pos: value for pos, value in knights.items() if len(value)}
n = 0
while knights:
    knight = sorted(knights.items(), key=lambda x: len(x[1]), reverse=True)[0][0]
    v = knights.pop(knight)
    n += 1
    for p in v:
        if p in knights:
            knights[p].remove(knight)
    knights = {pos: value for pos, value in knights.items() if len(value)}
print(n)
