# Input
text = input()

result = text[0]

# Logic
for ch in text:
    if ch == result[-1]:
        continue
    result += ch

# Output
print(result)
