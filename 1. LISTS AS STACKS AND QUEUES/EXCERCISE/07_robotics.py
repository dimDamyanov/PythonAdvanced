from collections import deque
from datetime import datetime, timedelta

END_COMMAND = 'End'

data = input().split(';')
time = datetime.strptime(input(), '%H:%M:%S')
robots = []

for el in data:
    robot_data = el.split('-')
    robot = {'name': robot_data[0], 'processing_time': int(robot_data[1]), 'available_at': time}
    robots.append(robot)

products = deque()
while True:
    command = input()
    if command == END_COMMAND:
        break
    else:
        products.append(command)

time += timedelta(seconds=1)
while products:
    current_product = products.popleft()
    flag = False
    for robot in robots:
        if robot['available_at'] <= time:
            robot['available_at'] = time + timedelta(seconds=robot['processing_time'])
            print(f'{robot["name"]} - {current_product} [{time.strftime("%H:%M:%S")}]')
            flag = True
            break
    if not flag:
        products.append(current_product)
    time += timedelta(seconds=1)
