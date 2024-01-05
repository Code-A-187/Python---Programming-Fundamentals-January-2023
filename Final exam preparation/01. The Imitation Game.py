encrypted_message = input()

data = input()

while data != 'Decode':
    splitted_data = data.split('|')
    command = splitted_data[0]

    if command == 'Move':
        n_letters = int(splitted_data[1])
        encrypted_message = encrypted_message[n_letters:] + encrypted_message[:n_letters]
    elif command == 'Insert':
        index = int(splitted_data[1])
        additional_string = splitted_data[2]
        encrypted_message = encrypted_message[:index] + additional_string + encrypted_message[index:]
    elif command == 'ChangeAll':
        sub_string = splitted_data[1]
        replacement_string = splitted_data[2]
        encrypted_message = encrypted_message.replace(sub_string, replacement_string)
    data = input()
print(f'The decrypted message is: {encrypted_message}')
