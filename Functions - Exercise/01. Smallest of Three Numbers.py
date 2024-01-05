def get_min_num(numbers):
    min_number = float('inf')
    for num in numbers:
        if num < min_number:
            min_number = num

    return min_number


first, second, third = int(input()), int(input()), int(input())

print(get_min_num([first, second, third]))
