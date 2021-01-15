n = int(input())
longest_intersection = []
for _ in range(n):
    tokens = input().split(',')
    first_start = int(tokens[0])
    first_end, second_start = map(int, tokens[1].split('-'))
    second_end = int(tokens[2])
    set_first = set(range(first_start, first_end+1))
    set_second = set(range(second_start, second_end+1))
    if len(set_first & set_second) > len(longest_intersection):
        longest_intersection = list(set_first & set_second)
print(f'Longest intersection is {longest_intersection} with length {len(longest_intersection)}')
