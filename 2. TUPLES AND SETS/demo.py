def get_indices(values, value):
    index = 0
    indices = []
    while True:
        try:
            new_index = values.index(value, index)
            indices.append(new_index)
            index = new_index + 1
        except ValueError:
            break
    return indices


print(get_indices((5, 8, 5, 8, 9, 5), 5))
