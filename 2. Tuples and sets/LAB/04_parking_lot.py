IN_COMMAND = 'IN'
OUT_COMMAND = 'OUT'

n = int(input())
parking_lot = set()
for i in range(n):
    command, car_number = input().split(', ')
    if command == IN_COMMAND:
        parking_lot.add(car_number)
    elif command == OUT_COMMAND:
        parking_lot.remove(car_number)

if parking_lot:
    print(*parking_lot, sep='\n')
else:
    print('Parking Lot is Empty')
