def list_abs(nums: list):
    return [abs(n) for n in nums]


ll = [float(n) for n in input().split()]
print(list_abs(ll))
