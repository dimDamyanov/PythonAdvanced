from math import log, e

n = int(input())
base = input()
if base == 'natural':
    print(f'{(log(n)):.2f}')
else:
    print(f'{(log(n, int(base))):.2f}')
