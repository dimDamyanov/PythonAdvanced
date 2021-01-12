clothes = list(map(int, input().split()))
capacity = int(input())
s = []
for c in clothes:
    s.append(c)

n = 1
current_capacity = capacity

while s:
    if s[-1] <= current_capacity:
        current_capacity -= s.pop()
    else:
        n += 1
        current_capacity = capacity

print(n)