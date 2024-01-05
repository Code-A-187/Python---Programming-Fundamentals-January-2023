# Input

number = int(input())

# Logic

for _ in range(number):
    word = input()
    is_pure = True
    for ch in word:
        if ch == "," or ch == '_' or ch == '.':
            is_pure = False
            break
    if is_pure:
        print(f'{word} is pure.')
    else:
        print(f'{word} is not pure!')

