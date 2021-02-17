from collections import deque

customers = deque(list(map(int, input().split(', '))))
taxis = list(map(int, input().split(', ')))

total_time = 0
while customers and taxis:
    current_customer = customers.popleft()
    current_taxi = taxis.pop()
    if current_taxi >= current_customer:
        total_time += current_customer
    else:
        customers.appendleft(current_customer)

if customers:
    print('Not all customers were driven to their destinations')
    print(f'Customers left: {", ".join([str(el) for el in customers])}')
else:
    print('All customers were driven to their destinations')
    print(f'Total time: {total_time} minutes')
