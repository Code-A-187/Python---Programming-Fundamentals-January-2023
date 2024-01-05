digits_list = input().split(' ')
string = input()

message = []

for el in digits_list:
    index = 0
    for digit in el:
        index += int(digit)

    index %= len(string)

    message.append(string[index])

    string = string.replace(string[index], '', 1)

print(''.join(message))
