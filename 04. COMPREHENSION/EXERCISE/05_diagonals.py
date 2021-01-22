rows = int(input())
matrix = [[int(num) for num in input().split(', ')] for _ in range(rows)]
primary_diagonal = [matrix[i][i] for i in range(rows)]
secondary_diagonal = [matrix[i][rows-i-1] for i in range(rows)]
print(f'First diagonal: {", ".join([str(num) for num in primary_diagonal])}. Sum: {sum(primary_diagonal)}')
print(f'Second diagonal: {", ".join([str(num) for num in secondary_diagonal])}. Sum: {sum(secondary_diagonal)}')
