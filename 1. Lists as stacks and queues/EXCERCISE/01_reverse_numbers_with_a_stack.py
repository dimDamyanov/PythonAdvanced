numbers = list(map(int, input().split()))
s = []
for num in numbers:
    s.append(num)
nums = []
while s:
    nums.append(s.pop())
print(' '.join([str(e) for e in nums]))
