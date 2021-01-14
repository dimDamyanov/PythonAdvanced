n = int(input())
names = []
for i in range(n):
    name = input()
    names.append(name)

unique_names = set(names)
print(*unique_names, sep='\n')