# Input

divisor = int(input())
bound = int(input())

result = 0

# Logic

for num in range(1, bound + 1):
    if num % divisor == 0:
        result = num
print(result)
