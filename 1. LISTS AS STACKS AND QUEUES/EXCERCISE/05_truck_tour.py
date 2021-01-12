from collections import deque

n = int(input())
pumps = []

for _ in range(n):
    pumps.append(list(map(int, input().split())))

queue = deque(pumps)
tour = pumps.copy()
ind = 0
while queue:
    tank = 0
    for i in range(n):
        petrol, distance = queue.popleft()
        tank += petrol

        if tank >= distance:
            tank -= distance
        else:
            queue = deque(tour)
            queue.append(queue.popleft())
            tour = list(queue)
            break
    ind += 1

print(ind-1)
