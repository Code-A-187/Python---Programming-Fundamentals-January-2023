# Input
text = input()
# Logic

encrypted_text = ''.join([chr(ord(ch) + 3) for ch in text])
# Output

print(encrypted_text)
