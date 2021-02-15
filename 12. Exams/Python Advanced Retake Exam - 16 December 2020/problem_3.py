def get_magic_triangle(n: int):
    triangle = []
    for i in range(n):
        if triangle:
            row = []
            for j in range(i + 1):
                if j == 0:
                    row.append(triangle[-1][0])
                elif j == i:
                    row.append(triangle[-1][-1])
                else:
                    row.append(triangle[-1][j - 1] + triangle[-1][j])
        else:
            row = [1]
        triangle.append(row)
    return triangle


print(get_magic_triangle(5))
