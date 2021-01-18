rows, cols = map(int, input().split(', '))
matrix = []
for _ in range(rows):
    row = list(map(int, input().split(', ')))
    matrix.append(row)

max_sum = 0
max_ind = [0, 0]

for i in range(rows-1):
    for j in range(cols-1):
        current_sum = 0
        current_sum += matrix[i][j]
        current_sum += matrix[i][j+1]
        current_sum += matrix[i+1][j]
        current_sum += matrix[i+1][j+1]
        if current_sum > max_sum:
            max_sum = current_sum
            max_ind = [i, j]

print(matrix[max_ind[0]][max_ind[1]], matrix[max_ind[0]][max_ind[1]+1])
print(matrix[max_ind[0]+1][max_ind[1]], matrix[max_ind[0]+1][max_ind[1]+1])
print(max_sum)
