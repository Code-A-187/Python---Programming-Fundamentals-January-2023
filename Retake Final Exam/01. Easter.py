string = input()

data = input()

while data != 'Easter':
    command_args = data.split()
    command = command_args[0]
    if command == 'Replace':
        current = command_args[1]
        new = command_args[2]
        string = string.replace(current, new)
        print(string)
    elif command == 'Remove':
        substr = command_args[1]
        string = string.replace(substr, '')
        print(string)
    elif command == 'Includes':
        sub_str = command_args[1]
        if sub_str in string:
            print('True')
        else:
            print('False')
    elif command == 'Change':
        upper_lower = command_args[1]
        if upper_lower == 'Lower':
            string = string.lower()
            print(string)
        else:
            string = string.upper()
            print(string)
    elif command == 'Reverse':
        start_index = int(command_args[1])
        end_index = int((command_args[2]))
        if 0 <= start_index < len(string) and 0 <= end_index < len(string):
            reversed_string = string[start_index:end_index + 1]
            print(reversed_string[::-1])
    data = input()