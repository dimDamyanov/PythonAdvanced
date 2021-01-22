END_COMMAND = 'End'

hero_names = input().split(', ')
heroes = {name: dict() for name in hero_names}
while True:
    command = input()
    if command == END_COMMAND:
        break
    else:
        args = command.split('-')
        if args[1] not in heroes[args[0]]:
            heroes[args[0]][args[1]] = int(args[2])
result = [f'{key} -> Items: {len(value)}, Cost: {sum(x for x in value.values())}' for key, value in heroes.items()]
for hero in result:
    print(hero)
