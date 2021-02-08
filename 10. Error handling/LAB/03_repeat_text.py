def repeat():
    text = input()
    count = int(input())
    return text * count


try:
    print(repeat())
except ValueError:
    print('Variable times must be an integer')
