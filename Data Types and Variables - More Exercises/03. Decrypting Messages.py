key = int(input())

line = int(input())

decrypted_message = []

for _ in range(line):
    char = input()
    decrypted_letter = ord(char) + key
    decrypted_message.append(chr(decrypted_letter))

print(''.join(decrypted_message))
