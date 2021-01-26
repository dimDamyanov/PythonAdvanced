def multiply(*args):
    prod = 1
    for num in args:
        prod *= num
    return prod


print(multiply(1, 5, 8))