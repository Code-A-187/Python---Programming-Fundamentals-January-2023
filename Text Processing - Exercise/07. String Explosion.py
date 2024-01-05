# Input
text = input()
parts = text.split('>')
previous = 0
result = [parts[0]]
# Logic
for part in parts[1:]:
    power = int(part[0])
    previous += power

    formatted_part = part[previous:]
    previous = max(previous - len(part), 0)
    result.append(formatted_part)
# Output
print('>'. join(result))
