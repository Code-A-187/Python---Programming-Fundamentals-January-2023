inventory = input().split(', ')

data = input()
while data != 'Craft!':
    command_args = data.split(' - ')
    command = command_args[0]
    item = command_args[1]
    if command == 'Collect':
        if item not in inventory:
            inventory.append(item)
    elif command == 'Drop':
        if item in inventory:
            inventory.remove(item)
    elif command == 'Combine Items':
        items = item.split(':')
        old_item = items[0]
        new_item = items[1]
        if items[0] in inventory:
            inventory.insert(inventory.index(old_item) + 1, new_item)
    elif command == 'Renew':
        if item in inventory:
            inventory.remove(item)
            inventory.append(item)
    data = input()

print(', '.join(inventory))
