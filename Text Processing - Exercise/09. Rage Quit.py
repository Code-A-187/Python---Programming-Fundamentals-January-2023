# Input
string = input()

result_string = ''

unique_chars = []
current_string = []

# Logic
for char in string:
    if char.isdigit():
        result_string += ''.join(current_string) * int(char)

        current_string.clear()
    else:
        current_string.append(char.upper())

for element in result_string:
    if element not in unique_chars:
        unique_chars.append(element)
    else:
        continue

# Output
print(f'Unique symbols used: {len(unique_chars)}')
print(result_string)
