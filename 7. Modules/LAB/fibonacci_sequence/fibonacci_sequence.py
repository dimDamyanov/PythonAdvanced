seq = [1, 0]


def create_sequence(n):
    global seq
    if n == 0:
        return []
    elif n == 1:
        return [0]
    else:
        seq = [0, 1]
        for _ in range(2, n):
            seq.append(seq[-1] + seq[-2])
        return seq


def locate(x):
    if x in seq:
        return seq.index(x)
    else:
        return
