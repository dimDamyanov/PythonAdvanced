def list_round(nums: list):
    return [round(n) for n in nums]


ll = [float(n) for n in input().split()]
print(list_round(ll))
