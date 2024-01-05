# Input
snowballs = int(input())

best_snowball = float('-inf')
output = ''
# Logic

for i in range(snowballs):
    weight = int(input())
    time = int(input())
    quality = int(input())

    result = (weight // time) ** quality

    if result > best_snowball:
        best_snowball = result
        output = f"{weight} : {time} = {result} ({quality})"
# Output
print(output)
