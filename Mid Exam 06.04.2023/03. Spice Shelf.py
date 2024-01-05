spices_list = input().split(', ')

data = input()

while data != 'done':
    command_args = data.split()
    command = command_args[0]
    if command == 'AddSpice':
        spice = command_args[1]
        if spice not in spices_list:
            spices_list.append(spice)
    elif command == 'AddManySpices':
        index = int(command_args[1])
        spicesToAdd = command_args[2].split('|')
        last_index = len(spicesToAdd)
        spices_list[index:last_index] = spicesToAdd
    elif command == 'SwapSpices':
        spice_one = command_args[1]
        spice_two = command_args[2]
        if spice_one in spices_list and spice_two in spices_list:
            a = spices_list.index(spice_one)
            b = spices_list.index(spice_two)
            spices_list[a], spices_list[b] = spices_list[b], spices_list[a]
    elif command == 'ThrowAwaySpices':
        start_spice = command_args[1]
        end_index = int(command_args[2])
        if start_spice in spices_list:
            start_index = spices_list.index(start_spice)
            del spices_list[start_index:start_index + end_index]
    elif data == 'Arrange':
        spices_list = sorted(spices_list, key=str.lower)
    data = input()
print(' '.join(spices_list))
