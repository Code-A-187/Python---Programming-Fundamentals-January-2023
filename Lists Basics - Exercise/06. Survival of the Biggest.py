list_of_int = input().split()
count = int(input())
numbers = []

for el in list_of_int:
    numbers.append(int(el))

for _ in range(count):
    min_number = min(numbers)
    numbers.remove(min_number)

for idx in range(len(numbers)):
    num = numbers[idx]
    if idx == len(numbers) - 1:
        print(num)
    else:
        print(num, end=', ')

