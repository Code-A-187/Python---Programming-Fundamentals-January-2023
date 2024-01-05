secret_messages = input().split()

secret_message = []

for part in secret_messages:
    digit = []
    word = []
    for char in part:
        if char.isdigit():
            digit.append(char)
        else:
            word.append(char)
    word[0], word[-1] = word[-1], word[0]
    number = ''.join(digit)
    word.insert(0, chr(int(number)))
    secret_message.append(''.join(word))

    digit.clear()
    word.clear()

print(' '.join(secret_message))
