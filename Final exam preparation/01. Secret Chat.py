message = input()

while True:
    line = input()
    if line == 'Reveal':
        break
    command_args = line.split(':|:')
    command = command_args[0]
    if command == 'InsertSpace':
        index = int(command_args[1])
        message = message[:index] + ' ' + message[index:]
        print(message)
    elif command == 'Reverse':
        substring = command_args[1]
        if substring not in message:
            print('error')
        else:
            message = message.replace(substring, '', 1)
            reversed_substring = ''.join(reversed(substring))
            message = message + reversed_substring
            print(message)
    elif command == 'ChangeAll':
        substring = command_args[1]
        replacement = command_args[2]
        message = message.replace(substring, replacement)
        print(message)

print(f"You have a new text message: {message}")
