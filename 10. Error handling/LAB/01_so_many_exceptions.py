numbers_list = input().split(', ')
result = 1

for i in range(len(numbers_list)):
    number = int(numbers_list[i])
    if number <= 5:
        result *= number
    else:
        result /= number

print(f'{result:.0f}')
