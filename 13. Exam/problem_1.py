from collections import deque


def remove_nonpositives(nums):
    return [n for n in nums if n > 0]


effects_list = list(map(int, input().split(', ')))
effects = deque(effects_list)
explosive_power = list(map(int, input().split(', ')))
fireworks = {
    'Palm': 0,
    'Willow': 0,
    'Crossette': 0
}

win_condition = False

effects = deque(remove_nonpositives(effects))
explosive_power = remove_nonpositives(explosive_power)
while effects and explosive_power:
    current_effect = effects.popleft()
    current_power = explosive_power.pop()
    while current_effect <= 0 and current_power <= 0:
        current_effect = effects.popleft()
    current_sum = current_effect + current_power
    if current_sum % 3 == 0 and current_sum % 5 != 0:
        fireworks['Palm'] += 1
    elif current_sum % 5 == 0 and current_sum % 3 != 0:
        fireworks['Willow'] += 1
    elif current_sum % 3 == 0 and current_sum % 5 == 0:
        fireworks['Crossette'] += 1
    else:
        current_effect -= 1
        effects.append(current_effect)
        explosive_power.append(current_power)

    if fireworks['Palm'] >= 3 and fireworks['Willow'] >= 3 and fireworks['Crossette'] >= 3:
        win_condition = True
        break

    effects = deque(remove_nonpositives(effects))
    explosive_power = remove_nonpositives(explosive_power)

if win_condition:
    print('Congrats! You made the perfect firework show!')
else:
    print('Sorry. You can’t make the perfect firework show.')
if effects:
    print(f'Firework Effects left: {", ".join([str(el) for el in effects])}')
if explosive_power:
    print(f'Explosive Power left: {", ".join([str(el) for el in explosive_power])}')

for key, value in fireworks.items():
    print(f'{key} Fireworks: {value}')

