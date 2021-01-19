from sys import maxsize


def read_row():
    return [int(el) for el in input().split()]


def sum_sub_matrix(matrix: list, element: tuple, sub_size: int):
    matrix_sum = 0
    for i in range(element[0], element[0]+sub_size):
        for j in range(element[1], element[1]+sub_size):
            matrix_sum += matrix[i][j]
    return matrix_sum


def print_sub_matrix(matrix: list, element: tuple, sub_size: int):
    for i in range(element[0], element[0]+sub_size):
        for j in range(element[1], element[1]+sub_size):
            print(matrix[i][j], end=' ')
        print()


size = [int(el) for el in input().split()]

max_sum = -maxsize
best_element = None

for i in range(size[0]):
    for j in range(size[1]):
        if (current_sum := sum_sub_matrix(matrix, (i, j), 3)) > max_sum:
            max_sum = current_sum
            best_element = i, j


print(f'Sum = {max_sum}')
print_sub_matrix(matrix, best_element, 3)
