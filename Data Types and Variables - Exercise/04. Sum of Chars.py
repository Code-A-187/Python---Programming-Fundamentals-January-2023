# Input
char = int(input())
result = 0
# Logic
for _ in range(char):
    symbol = input()
    result += ord(symbol)
# Output
print(f"The sum equals: {result}")
