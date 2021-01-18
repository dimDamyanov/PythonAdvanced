n = int(input())
matrix = []
for _ in range(n):
    row = input()
    matrix.append(row)
flag = False
symbol = input()
for i in range(n):
    if symbol in matrix[i]:
        print(f'({i}, {matrix[i].find(symbol)})')
        flag = True
        break

if not flag:
    print(f'{symbol} does not occur in the matrix')
