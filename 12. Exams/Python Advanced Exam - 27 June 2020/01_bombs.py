from collections import deque


def check_pouch(pouch: dict):
    if len(pouch) == 3:
        for b_quantity in pouch.values():
            if b_quantity < 3:
                return False
    else:
        return False
    return True


effect_list = list(map(int, input().split(', ')))
effects = deque(effect_list)
casings = list(map(int, input().split(', ')))

bomb_mapper = {
    40: 'Datura',
    60: 'Cherry',
    120: 'Smoke Decoy'
}

bombs = {
    'Datura': 0,
    'Cherry': 0,
    'Smoke Decoy': 0
}

win_flag = False
while effects and casings:
    current_effect = effects.popleft()
    current_casing = casings.pop()
    while True:
        current_sum = current_effect + current_casing
        if current_sum in bomb_mapper:
            bomb_type = bomb_mapper[current_sum]
            if bomb_type not in bombs:
                bombs[bomb_type] = 0
            bombs[bomb_type] += 1
            break
        else:
            current_casing -= 5
    if check_pouch(bombs):
        win_flag = True
        break

if win_flag:
    print('Bene! You have successfully filled the bomb pouch!')
else:
    print('You don\'t have enough materials to fill the bomb pouch.')
if effects:
    print(f'Bomb Effects: {", ".join(list(map(str, effects)))}')
else:
    print('Bomb Effects: empty')
if casings:
    print(f'Bomb Casings: {", ".join(map(str, casings))}')
else:
    print('Bomb Casings: empty')
bombs = sorted(bombs.items(), key=lambda x: x[0])
for bomb_type, quantity in bombs:
    print(f'{bomb_type} Bombs: {quantity}')
