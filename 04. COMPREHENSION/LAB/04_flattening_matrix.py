rows = int(input())
matrix = [list(map(int, input().split(', '))) for _ in range(rows)]
flattened_matrix = [num for row in matrix for num in row]
print(flattened_matrix)
