lines = int(input())

is_balanced = True

last_bracket = ''
for _ in range(lines):
    message = input()
    if message not in ['(', ')']:
        continue
    else:
        if last_bracket == '' and message == ')' or last_bracket == message:
            is_balanced = False
            break

    last_bracket = message

if is_balanced:
    print('BALANCED')

else:
    print('UNBALANCED')
