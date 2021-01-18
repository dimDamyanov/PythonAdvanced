rows, cols = map(int, input().split(', '))
matrix = []
for _ in range(rows):
    row = list(map(int, input().split(' ')))
    matrix.append(row)

col_sums = []
for i in range(cols):
    col_sums.append(0)
    for j in range(rows):
        col_sums[-1] += matrix[j][i]

for col_sum in col_sums:
    print(col_sum)
