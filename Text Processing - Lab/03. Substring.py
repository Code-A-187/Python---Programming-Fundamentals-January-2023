# Input
sub_text = input()
text = input()

# Logic
while sub_text in text:
    text = text.replace(sub_text, "")

# Print
print(text)
