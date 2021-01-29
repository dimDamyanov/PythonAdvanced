def heapPermutation(a, size):
    if size == 1:
        print(*a, sep='')
    for i in range(size):
        heapPermutation(a, size-1)
        if size & 1:
            a[0], a[size-1] = a[size-1], a[0]
        else:
            a[i], a[size-1] = a[size-1], a[i]


chars = [ch for ch in input()]
heapPermutation(chars, len(chars))