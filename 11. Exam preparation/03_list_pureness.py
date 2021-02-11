from collections import deque


def best_list_pureness(nums_list: list, k: int):
    nums = deque(nums_list)
    best_pureness = 0
    best_pureness_rotations = 0
    for i in range(k + 1):
        current_sum = 0
        for ind, num in enumerate(nums):
            current_sum += ind * num
        if current_sum > best_pureness:
            best_pureness = current_sum
            best_pureness_rotations = i
        print(f'{i} => {current_sum}')
        nums.appendleft(nums.pop())
    return f'Best pureness {best_pureness} after {best_pureness_rotations} rotations'


test = ([7, 9, 2, 5, 3, 4], 3)
result = best_list_pureness(*test)
print(result)


