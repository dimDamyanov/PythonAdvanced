def detonate(matrix: list, r: int, c: int):
    if matrix[r][c] > 0:
        affected = {(r - 1, c - 1), (r, c - 1), (r + 1, c - 1), (r + 1, c), (r + 1, c + 1), (r, c + 1), (r - 1, c + 1),
                    (r - 1, c)}
        for pos in affected:
            if 0 <= pos[0] < len(matrix) and 0 <= pos[1] < len(matrix) and matrix[pos[0]][pos[1]] > 0:
                matrix[pos[0]][pos[1]] -= matrix[r][c]
        matrix[r][c] = 0


n = int(input())
grid = [[int(n) for n in input().split()] for _ in range(n)]
bombs = [tuple(int(x) for x in b.split(',')) for b in input().split()]
for bomb in bombs:
    detonate(grid, *bomb)
alive = [x for row in grid for x in row if x > 0]
print(f'Alive cells: {len(alive)}')
print(f'Sum: {sum(alive)}')
for row in grid:
    print(*row, sep=' ')
print()
