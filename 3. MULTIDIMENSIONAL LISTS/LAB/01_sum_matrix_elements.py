rows, cols = map(int, input().split(', '))
matrix = []
for _ in range(rows):
    row = list(map(int, input().split(', ')))
    matrix.append(row)

matrix_sum = 0
for i in range(rows):
    for j in range(cols):
        matrix_sum += matrix[i][j]
print(matrix_sum)
print(matrix)
