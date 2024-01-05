import re

text = input()
matches = re.findall(r'([#@])([A-Za-z]{3,})(\1{2})([A-Za-z]{3,})(\1)', text)

mirror_pairs = []

for match in matches:
    first_word = match[1]
    second_word = match[3]
    if first_word == second_word[::-1]:
        mirror_pairs.append(first_word + " <=> " + second_word)
if not len(matches):
    print("No word pairs found!")
else:
    print(f'{len(matches)} word pairs found!')

if not len(mirror_pairs):
    print("No mirror words!")
else:
    print(f"The mirror words are:\n{', '.join(mirror_pairs)}")
