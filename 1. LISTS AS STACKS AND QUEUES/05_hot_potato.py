from collections import deque

kids_queue = deque()

kids = input().split()
for kid in kids:
    kids_queue.append(kid)
step = int(input())

# i = 0
# while len(kids_queue) > 1:
#     i += 1
#     current_player = kids_queue.popleft()
#     if i == step:
#         print(f'Removed {current_player}')
#         i = 0
#     else:
#         kids_queue.append(current_player)

while len(kids_queue) > 1:
    for _ in range(step-1):
        kids_queue.append(kids_queue.popleft())
    print(f'Removed {kids_queue.popleft()}')
print(f'Last is {kids_queue.popleft()}')
