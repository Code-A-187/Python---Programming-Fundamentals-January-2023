activation_key = input()

data = input()

while data != 'Generate':
    splitted_string = data.split('>>>')
    command = splitted_string[0]
    if command == 'Contains':
        substring = splitted_string[1]
        if substring in activation_key:
            print(f"{activation_key} contains {substring}")
        else:
            print("Substring not found!")
    elif command == 'Flip':
        upper_lower = splitted_string[1]
        start_index = int(splitted_string[2])
        end_index = int(splitted_string[3])
        if upper_lower == 'Upper':
            activation_key = activation_key[:start_index] + activation_key[start_index:end_index].upper() \
                             + activation_key[end_index:]
            print(activation_key)
        elif upper_lower == 'Lower':
            activation_key = activation_key[:start_index] + activation_key[start_index:end_index].lower() \
                             + activation_key[end_index:]
            print(activation_key)
    elif command == 'Slice':
        start_index = int(splitted_string[1])
        end_index = int(splitted_string[2])
        activation_key = activation_key[:start_index] + activation_key[end_index:]
        print(activation_key)
    data = input()

print(f'Your activation key is: {activation_key}')
