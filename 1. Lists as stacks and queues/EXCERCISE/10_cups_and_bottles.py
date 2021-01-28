from collections import deque

cups_map = map(int, input().split())
bottles = list(map(int, input().split()))
cups = deque(cups_map)
wasted_water = 0

while cups and bottles:
    current_bottle = bottles.pop()
    current_cup = cups.popleft()
    if current_bottle < current_cup:
        cups.appendleft(current_cup - current_bottle)
    else:
        wasted_water += current_bottle - current_cup

if bottles:
    bottles.reverse()
    print(f'Bottles: {" ".join([str(el) for el in bottles])}')
else:
    print(f'Cups: {" ".join([str(el) for el in cups])}')
print(f'Wasted litters of water: {wasted_water}')
