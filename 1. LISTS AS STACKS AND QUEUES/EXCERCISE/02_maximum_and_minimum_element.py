PUSH_COMMAND = '1'
DELETE_COMMAND = '2'
MAXIMUM_COMMAND = '3'
MINIMUM_COMMAND = '4'

n = int(input())

s = []
for _ in range(n):
    command = input()
    if command.startswith(PUSH_COMMAND):
        s.append(int(command.split()[1]))
    elif len(s) > 0:
        if command == DELETE_COMMAND:
            s.pop()
        elif command == MAXIMUM_COMMAND:
            print(max(s))
        elif command == MINIMUM_COMMAND:
            print(min(s))

nums = []
while s:
    nums.append(s.pop())
print(', '.join([str(e) for e in nums]))
