values = map(float, input().split())

values_counts = {}
for value in values:
    if value in values_counts:
        values_counts[value] += 1
    else:
        values_counts[value] = 1

for value, count in values_counts.items():
    print(f'{value} - {count} times')