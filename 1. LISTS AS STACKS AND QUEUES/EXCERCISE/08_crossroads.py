from collections import deque

END_COMMAND = 'END'
GREEN_COMMAND = 'green'

green_light = int(input())
free_window = int(input())

queue = deque()
n = 0
while True:
    line = input()
    if line == END_COMMAND:
        break
    elif line == GREEN_COMMAND:
        i = 0
        while i < green_light:
            current_car = queue.popleft()
            if green_light - i >= len(queue[0]):
                queue.popleft()
            i += 1

    else:
        queue.append(line)