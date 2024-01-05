import re

data = int(input())

pattern = r'(!)([A-Z][A-z]{2,})\1:([)([A-Z][A-z]{7,})(])'

for _ in range(data):
    string = input()
    numeric_list = []
    if re.match(pattern, string):
        message_args = string.split('!:[')
        command_part = message_args[0]
        message_part = message_args[1]
        command = command_part.replace("!", "")
        for char in message_part:
            if char.isalpha():
                numeric_list.append(str(ord(char)))
        print(f"{command}: {' '.join(numeric_list)}")
    else:
        print('The message is invalid')
