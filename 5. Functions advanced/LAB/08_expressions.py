def expressions(nums, current_sum=0, expression=''):
    if not nums:
        return [(expression, current_sum)]
    result_plus = expressions(nums[1:], current_sum+nums[0], f'{expression}+{nums[0]}')
    result_minus = expressions(nums[1:], current_sum-nums[0], f'{expression}-{nums[0]}')
    return result_plus + result_minus


nums = [int(el) for el in input().split(', ')]
print(*[f'{exp}={res}' for exp, res in expressions(nums)], sep='\n')
