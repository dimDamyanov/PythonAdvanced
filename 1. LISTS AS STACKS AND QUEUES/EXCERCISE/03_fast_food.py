from collections import deque


def print_left(queue: deque):
    left = list(queue)
    print(f'Orders left: {" ".join([str(e) for e in left])}')


quantity = int(input())
flag = False
orders = list(map(int, input().split()))
order_queue = deque()
for order in orders:
    order_queue.append(order)

print(max(order_queue))
while order_queue:
    order = order_queue[0]
    if order <= quantity:
        quantity -= order_queue.popleft()
    else:
        flag = True
        print_left(order_queue)
        break
if not flag:
    print('Orders complete')
