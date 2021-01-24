def vulnerable_positions(grid, y: int, x: int):
    vulnerable = [(y-2, x+1), (y-1, x+2), (y+1, x+2), (y+2, x+1), (y+2, x-1), (y+1, x-2), (y-1, x-2), (y+2, x-1)]
    count = 0
    for r, c in vulnerable:
        if 0 <= r < n and 0 <= c < n:
            if grid[r][c] == 'K':
                count += 1
    return count


n = int(input())
matrix = [[ch for ch in input()] for _ in range(n)]
knights = dict()
for i in range(n):
    for j in range(n):
        if matrix[i][j] == 'K':
            knights[i, j] = vulnerable_positions(matrix, i, j)
knights = sorted(knights.items(), key=lambda x: -x[1])
print(knights)

for row, col, _ in knights:
    matrix[row[0]][col[1]] = '0'
    knights = dict()
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 'K':
                knights[i, j] = vulnerable_positions(matrix, i, j)

