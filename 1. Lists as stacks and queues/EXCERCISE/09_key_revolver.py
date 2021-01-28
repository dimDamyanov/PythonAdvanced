from collections import deque

bullet_price = int(input())
barrel_size = int(input())
bullets = list(map(int, input().split()))
locks = list(map(int, input().split()))
intelligence_value = int(input())
fired_bullets = 0
barrel = deque()

for _ in range(barrel_size):
    if bullets:
        barrel.append(bullets.pop())

while (bullets or barrel) and locks:
    current_bullet = barrel.popleft()
    fired_bullets += 1
    if current_bullet <= locks[0]:
        locks.pop(0)
        print('Bang!')
    else:
        print('Ping!')

    if not barrel:
        if bullets:
            print('Reloading!')
            for _ in range(barrel_size):
                if bullets:
                    barrel.append(bullets.pop())
                else:
                    break
        else:
            break

if locks:
    print(f'Couldn\'t get through. Locks left: {len(locks)}')
else:
    print(f'{len(bullets) + len(barrel)} bullets left. Earned ${intelligence_value - fired_bullets * bullet_price}')