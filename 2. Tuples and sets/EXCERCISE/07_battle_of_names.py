n = int(input())
odd_set = set()
even_set = set()
for i in range(n):
    name = input()
    ord_sum = 0
    for ch in name:
        ord_sum += ord(ch)
    ord_sum //= (i+1)
    if ord_sum % 2 == 0:
        even_set.add(ord_sum)
    else:
        odd_set.add(ord_sum)

if sum(odd_set) > sum(even_set):
    print(', '.join([str(e) for e in odd_set - even_set]))
elif sum(odd_set) < sum(even_set):
    print(', '.join([str(e) for e in odd_set ^ even_set]))
else:
    print(', '.join([str(e) for e in odd_set | even_set]))