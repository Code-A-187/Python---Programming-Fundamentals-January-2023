# Input
text = input()

letters = ""
digits = ""
symbols = ""

# Logic
for char in text:
    if char.isalpha():
        letters += char
    elif char.isdigit():
        digits += char
    else:
        symbols += char
# Output

print(digits)
print(letters)
print(symbols)
