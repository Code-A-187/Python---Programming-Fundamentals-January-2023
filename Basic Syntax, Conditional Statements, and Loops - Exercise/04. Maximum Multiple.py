# Input

divisor = int(input())
bound = int(input())

result = 0

# Logic

for num in range(bound, 0, -1):
    if num % divisor == 0:
        print(num)
        break
