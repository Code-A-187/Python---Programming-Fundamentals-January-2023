# Input
banned_words = input().split(", ")
text = input()

# Logic

for word in banned_words:
    text = text.replace(word, "*"*len(word))

# Output
print(text)
