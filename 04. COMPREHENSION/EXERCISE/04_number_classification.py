nums = list(map(int, input().split(', ')))
positive_nums = [num for num in nums if num >= 0]
negative_nums = [num for num in nums if num < 0]
even_nums = [num for num in nums if num % 2 == 0]
odd_nums = [num for num in nums if num % 2 == 1]
print(f'Positive: {", ".join([str(num) for num in positive_nums])}')
print(f'Negative: {", ".join([str(num) for num in negative_nums])}')
print(f'Even: {", ".join([str(num) for num in even_nums])}')
print(f'Odd: {", ".join([str(num) for num in odd_nums])}')
