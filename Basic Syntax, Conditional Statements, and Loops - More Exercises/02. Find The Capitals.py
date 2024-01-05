word = input()

idx_list = []

for char in range(len(word)):
    if word[char].isupper():
        idx_list.append(char)

print(idx_list)
