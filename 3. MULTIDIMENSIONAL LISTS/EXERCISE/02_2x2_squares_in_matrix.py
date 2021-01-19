rows, cols = map(int, input().split())
matrix = []
for _ in range(rows):
    row = input().split()
    matrix.append(row)
n = 0
for i in range(rows-1):
    for j in range(cols-1):
        if matrix[i][j] == matrix[i+1][j]:
            if matrix[i+1][j] == matrix[i+1][j+1]:
                if matrix[i+1][j+1] == matrix[i][j+1]:
                    n += 1
print(n)
