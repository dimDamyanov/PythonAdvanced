END_COMMAND = 'END'

n = int(input())
reservations = set()
arrived = set()

for i in range(n):
    reservation_num = input()
    reservations.add(reservation_num)

while True:
    command = input()
    if command == END_COMMAND:
        break
    else:
        arrived.add(command)

not_arrived = reservations - arrived
print(len(not_arrived))
vip_guests = []
regular_guests = []
for guest in not_arrived:
    if guest[0].isdigit():
        vip_guests.append(guest)
    else:
        regular_guests.append(guest)
vip_guests.sort()
regular_guests.sort()
if vip_guests:
    print(*vip_guests, sep='\n')
if regular_guests:
    print(*regular_guests, sep='\n')