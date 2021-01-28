categories = input().split(', ')
items = {category: [] for category in categories}
n = int(input())
for _ in range(n):
    args = input().split(' - ')
    quantity, quality = [int(x.split(':')[1]) for x in args[2].split(';')]
    items[args[0]].append({args[1]: (quantity, quality)})
count = sum(data[0] for cat in items.values() for item in cat for data in list(item.values()))
quality_sum = sum(data[1] for cat in items.values() for item in cat for data in list(item.values()))
print(f'Count of items: {count}')
print(f'Average quality: {(quality_sum/len(items)):.2f}')
for cat, value in items.items():
    print(f'{cat} -> {", ".join([list(item.keys())[0] for item in value])}')
