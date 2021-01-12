from datetime import datetime, timedelta
from collections import deque

END_COMMAND = 'End'

robots = {}
line = input().split(';')

for entry in line:
    tokens = entry.split('-')
    robot = tokens[0]
    processing_time = int(tokens[1])
    busy_time =
    robots[robot] = processing_time

current_time = datetime.strptime(input(), '%H:%M:%S')

products = deque()
while True:
    command = input()
    if command == END_COMMAND:
        break
    else:
        products.append(command)

while products:
