n = int(input())
elements = set()
for _ in range(n):
    compound = input().split()
    for el in compound:
        elements.add(el)
for el in elements:
    print(el)