def even_odd(*args):
    arguments = [arg for arg in args]
    command = arguments.pop()
    mapper = {
        'odd': lambda x: x % 2 != 0,
        'even': lambda x: x % 2 == 0
    }
    return list(filter(mapper[command], arguments))


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
