import re

namePattern = r'@(?P<name>[A-Za-z]+)\|'
agePattern = r'#(?P<age>[0-9]+)\*'

line = int(input())

for _ in range(line):
    data = input()
    name = re.findall(namePattern, data)
    age = re.findall(agePattern, data)
    print(f"{''.join(name)} is {''.join(age)} years old.")
