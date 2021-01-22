import timeit


def test(n: int):
    test_setup64 = f'll = [1] * (1 << {n})'
    reversed_test = 'list(reversed(ll))'
    slicing_test = 'list(ll[::-1])'

    print(f'{1 << n} elements')
    reversed_time = timeit.timeit(stmt=reversed_test, setup=test_setup64)
    slicing_time = timeit.timeit(stmt=slicing_test, setup=test_setup64)
    print('reversed:', reversed_time)
    print('slicing:', slicing_time)
    if reversed_time < slicing_time:
        print(f'winner: reversed(), dt= {abs(slicing_time-reversed_time)}')
    else:
        print(f'winner: [::-1], dt= {abs(slicing_time-reversed_time)}')
    print('-' * 40)


for i in range(4, 10):
    test(i)