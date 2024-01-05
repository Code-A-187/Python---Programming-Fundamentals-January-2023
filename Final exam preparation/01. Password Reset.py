string = input()

data = input()
raw_password = string

while data != 'Done':
    if data == 'TakeOdd':
        current_pasword = raw_password
        raw_password = ''
        for char in range(len(current_pasword)):
            if char % 2 != 0:
                letter = current_pasword[char]
                raw_password += letter
        print(raw_password)
    else:
        splitted_data = data.split()
        command = splitted_data[0]
        if command == 'Cut':
            index = int(splitted_data[1])
            length = int(splitted_data[2])
            raw_password = raw_password[: index] + raw_password[index + length:]
            print(raw_password)
        elif command == 'Substitute':
            substring = splitted_data[1]
            substitute = splitted_data[2]
            if substring not in raw_password:
                print('Nothing to replace!')
            else:
                raw_password = raw_password.replace(substring, substitute)
                print(raw_password)
    data = input()
print(f'Your password is: {raw_password}')
