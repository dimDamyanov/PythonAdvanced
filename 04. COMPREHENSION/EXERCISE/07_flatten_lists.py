line = input()
nums = [num for sublist in reversed(line.split('|')) for num in sublist.split()]
print(' '.join(str(num) for num in nums))
