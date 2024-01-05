treasure_chest = input().split('|')

data = input()

while data != 'Yohoho!':
    command_args = data.split()
    command = command_args[0]
    if command == 'Loot':
        command_args.remove(command)
        for item in command_args:
            if item not in treasure_chest:
                treasure_chest.insert(0, item)
    elif command == 'Drop':
        index = int(command_args[1])
        if index <= len(treasure_chest):
            treasure_chest.append(treasure_chest.pop(index))
    elif command == 'Steal':
        index = int(command_args[1])
        if len(treasure_chest) <= index:
            print(', '.join(treasure_chest))
            treasure_chest.clear()
        else:
            print(', '.join(treasure_chest[-index:]))
            del treasure_chest[len(treasure_chest) - index:]

    data = input()


if len(treasure_chest) <= 0:
    print(f'Failed treasure hunt.')

else:
    items_lenght = 0
    for item in treasure_chest:
        items_lenght += len(item)
    treasure_gain = items_lenght / len(treasure_chest)
    print(f'Average treasure gain: {treasure_gain:.2f} pirate credits.')
