def get_row():
    return [int(el) for el in input().split()]


def sum_sub_matrix(main_matrix, element, size):
    my_sum = 0
    for i in range(element[0], element[0]+size):
        for j in range(element[1], element[1]+size):
            my_sum += main_matrix[i][j]
    return my_sum


def print_sub_matrix(main_matrix, element, size):
    for i in range(element[0], element[0] + size):
        for j in range(element[1], element[1] + size):
            print(main_matrix[i][j], end=' ')
        print()


rows, cols = get_row()
matrix = [get_row() for _ in range(rows)]
max_sum = sum_sub_matrix(matrix, (0, 0), 3)
max_sum_element = 0, 0
size = 3

for i in range(rows-size+1):
    for j in range(cols-size+1):
        current_sum = sum_sub_matrix(matrix, (i, j), 3)
        if current_sum > max_sum:
            max_sum = current_sum
            max_sum_element = i, j

print(f'Sum = {max_sum}')
print_sub_matrix(matrix, max_sum_element, 3)
