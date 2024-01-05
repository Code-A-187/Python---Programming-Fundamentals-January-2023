string = input()

forbidden_letters = ['a', 'o', 'u', 'e', 'i']

result = [char for char in string if char.lower() not in forbidden_letters]

print(''.join(result))

# for char in string:
#     if char.lower() not in ['a', 'o', 'u', 'e', 'i']:
#         result.append(char)


