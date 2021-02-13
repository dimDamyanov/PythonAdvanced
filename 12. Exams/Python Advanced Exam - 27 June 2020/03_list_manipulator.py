from collections import deque


def list_manipulator(numbers: list, command: str, position: str, *args):
    nums = deque(numbers)
    if command == 'add':
        if position == 'beginning':
            for num in reversed(args):
                nums.appendleft(num)
        elif position == 'end':
            for num in args:
                nums.append(num)
    elif command == 'remove':
        if position == 'beginning':
            if args:
                for _ in range(args[0]):
                    nums.popleft()
            else:
                nums.popleft()
        elif position == 'end':
            if args:
                for _ in range(args[0]):
                    nums.pop()
            else:
                nums.pop()
    return list(nums)


print(list_manipulator([1,2,3], "remove", "end"))
print(list_manipulator([1,2,3], "remove", "beginning"))
print(list_manipulator([1,2,3], "add", "beginning", 20))
print(list_manipulator([1,2,3], "add", "end", 30))
print(list_manipulator([1,2,3], "remove", "end", 2))
print(list_manipulator([1,2,3], "remove", "beginning", 2))
print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))
