def numbers_searching(*args):
    nums = sorted(args)
    duplicates = []
    [duplicates.append(num) for num in nums if nums.count(num) > 1 and num not in duplicates]
    seq = []
    [seq.append(num) for num in nums if num not in seq]
    missing = None
    for i in range(len(seq) - 1):
        if seq[i] + 1 != seq[i + 1]:
            missing = seq[i] + 1
    return [missing, duplicates]


print(numbers_searching(1, 2, 4, 2, 5, 4))
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))
