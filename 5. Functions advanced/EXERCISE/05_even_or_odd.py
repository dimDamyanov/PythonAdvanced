command = input()
nums = list(map(int, input().split()))
mapper = {
    'Odd': lambda x: x % 2 != 0,
    'Even': lambda x: x % 2 == 0
}
print(len(nums) * sum(list(filter(mapper[command], nums))))
