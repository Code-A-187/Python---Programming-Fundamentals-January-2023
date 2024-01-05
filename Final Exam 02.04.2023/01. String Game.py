string = input()

data = input()

while data != 'Done':
    command_args = data.split()
    command = command_args[0]

    if command == 'Change':
        char = command_args[1]
        replacement = command_args[2]
        string = string.replace(char, replacement)
        print(string)
    elif command == 'Includes':
        substring = command_args[1]
        if substring not in string:
            print('False')
        else:
            print('True')
    elif command == 'End':
        substring = command_args[1]
        ends_with = string.endswith(substring)
        print(ends_with)
    elif command == 'Uppercase':
        string = string.upper()
        print(string)
    elif command == 'FindIndex':
        char = command_args[1]
        print(string.index(char))
    elif command == 'Cut':
        start_index = int(command_args[1])
        count = int(command_args[2])
        end_index = start_index + count
        string = string[start_index:end_index]
        print(string)
    data = input()
