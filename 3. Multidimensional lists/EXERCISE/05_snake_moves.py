rows, cols = map(int, input().split())
matrix = []
snake_string = input()
ind = 0

for i in range(rows):
    row = []
    for j in range(cols):
        if i % 2 == 0:
            row.append(snake_string[ind])
        else:
            row.insert(0, snake_string[ind])
        ind += 1
        if ind == len(snake_string):
            ind = 0
    matrix.append(row)

for i in range(rows):
    for j in range(cols):
        print(matrix[i][j], end='')
    print()
