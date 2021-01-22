r, c = map(int, input().split())
words = [[f'{chr(97+i)}{chr(97+i+j)}{chr(97+i)}' for j in range(c)] for i in range(r)]
for row in words:
    print(' '.join(row))
