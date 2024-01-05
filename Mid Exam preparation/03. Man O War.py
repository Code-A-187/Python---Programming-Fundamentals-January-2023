pirate_ship = [int(x) for x in input().split('>')]
warship = [int(x) for x in input().split('>')]
max_health = int(input())

data = input()

stalemate = True

while data != 'Retire':
    command_args = data.split()
    command = command_args[0]
    if command == 'Fire':
        index = int(command_args[1])
        damage = int(command_args[2])
        if len(warship) > index >= 0:
            warship[index] -= damage
            if warship[index] <= 0:
                print(f'You won! The enemy ship has sunken.')
                stalemate = False
                break
    elif command == 'Defend':
        start_index = int(command_args[1])
        end_index = int(command_args[2])
        damage = int(command_args[3])
        if 0 <= start_index < len(pirate_ship) and 0 <= end_index < len(pirate_ship) and damage > 0:
            for index in range(start_index, end_index + 1):
                pirate_ship[index] -= damage
                if pirate_ship[index] <= 0:
                    print(f'You lost! The pirate ship has sunken.')
                    stalemate = False
                    break
    elif command == 'Repair':
        index = int(command_args[1])
        health = int(command_args[2])
        if 0 <= index < len(pirate_ship) and health > 0:
            pirate_ship[index] = min(pirate_ship[index] + health, max_health)
    elif command == 'Status':
        repair_needed = 0
        repair_health = max_health * 0.2
        for section in pirate_ship:
            if section < repair_health:
                repair_needed += 1
        print(f'{repair_needed} sections need repair.')

    data = input()

if stalemate:
    print(f'Pirate ship status: {sum(pirate_ship)}\nWarship status: {sum(warship)}')
