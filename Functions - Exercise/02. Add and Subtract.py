def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


first, second, third = int(input()), int(input()), int(input())

sum_result = (add(first, second))
result = (subtract(sum_result, third))

print(result)
