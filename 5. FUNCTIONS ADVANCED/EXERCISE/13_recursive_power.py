def recursive_power(n, a):
    if a == 0:
        return 1
    else:
        return n * recursive_power(n, a - 1)


print(recursive_power(2, 10))
print(recursive_power(10, 100))