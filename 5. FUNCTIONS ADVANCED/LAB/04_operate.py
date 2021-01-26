from functools import reduce


def operate(operator: str, *args):
    return reduce(lambda x, y: eval(f'{x} {operator} {y}'), args)


print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))
