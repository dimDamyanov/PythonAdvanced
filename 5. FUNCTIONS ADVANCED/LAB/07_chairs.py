def combinations(lst, n):
    if n == 0:
        return [[]]
    result = []
    for i in range(0, len(lst)):

        m = lst[i]
        rem_lst = lst[i + 1:]

        for p in combinations(rem_lst, n - 1):
            result.append([m] + p)

    return result


names = input().split(', ')
c = int(input())
print(*[', '.join(comb) for comb in combinations(names, c)], sep='\n')
