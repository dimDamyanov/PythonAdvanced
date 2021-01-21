rows = int(input())
matrix = [list(map(int, input().split(', '))) for _ in range(rows)]
even_matrix = [[num for num in row if num % 2 == 0] for row in matrix]
print(even_matrix)