list = input().split('!')

data = input()

while data != 'Go Shopping!':
    command_args = data.split()
    command = command_args[0]
    if command == 'Urgent':
        item = command_args[1]
        if item not in list:
            list.insert(0, item)
    elif command == 'Unnecessary':
        item = command_args[1]
        if item in list:
            list.remove(item)
    elif command == 'Correct':
        old_item = command_args[1]
        new_item = command_args[2]
        if old_item in list:
            list = [new_item if item == old_item else item for item in list]
    elif command == 'Rearrange':
        item = command_args[1]
        if item in list:
            list.append(list.pop(list.index(item)))
    data = input()
print(f"{', '.join(list)}")
