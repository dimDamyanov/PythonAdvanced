n = int(input())
matrix = []

for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

primary_diagonal = 0
secondary_diagonal = 0
for i in range(n):
    primary_diagonal += matrix[i][i]
    secondary_diagonal += matrix[i][n-i-1]
print(abs(primary_diagonal-secondary_diagonal))
