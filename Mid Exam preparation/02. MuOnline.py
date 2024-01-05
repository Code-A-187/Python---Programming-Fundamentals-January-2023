rooms_list = input().split('|')

health = 100
bitcoins = 0

survived = True

for room in rooms_list:
    command_args = room.split()
    command = command_args[0]
    points = int(command_args[1])
    if command == 'potion':
        current_health = health
        health = min(health + points, 100)
        print(f'You healed for {health - current_health} hp.')
        print(f'Current health: {health} hp.')
    elif command == 'chest':
        bitcoins += points
        print(f'You found {points} bitcoins.')
    else:
        health -= points
        if health > 0:
            print(f'You slayed {command}.')
        else:
            survived = False
            print(f'You died! Killed by {command}.')
            print(f'Best room: {rooms_list.index(room) + 1}')
            break

if survived:
    print(f"You've made it!\nBitcoins: {bitcoins}\nHealth: {health}")
