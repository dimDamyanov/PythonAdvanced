class ValueCannotBeNegativeError(Exception):
    def __init__(self, value):
        super().__init__(f'{value} is negative')
    pass


numbers = [int(input()) for _ in range(5)]

for number in numbers:
    if number < 0:
        raise ValueCannotBeNegativeError(number)
