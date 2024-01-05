targets = [int(x) for x in input().split()]

data = input()

while data != 'End':
    command_args = data.split()
    command = command_args[0]
    index = int(command_args[1])
    if command == 'Shoot':
        power = int(command_args[2])
        if index in range(len(targets)):
            targets[index] -= power
            if targets[index] <= 0:
                targets.pop(index)
    elif command == 'Add':
        value = int(command_args[2])
        if index in range(len(targets)):
            targets.insert(index, value)
        else:
            print("Invalid placement!")
    elif command == 'Strike':
        radius = int(command_args[2])
        start = index - radius
        end = index + radius
        if start >= 0 and end < len(targets):
            del targets[start: end]
        else:
            print('Strike missed!')
    data = input()

print("|".join(map(str, targets)))
