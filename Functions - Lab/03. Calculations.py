# Input
def solve(operator, a, b):
    result = 0
    if operator == "multiply":
        result = a * b
    elif operator == "divide":
        result = a // b
    elif operator == "add":
        result = a + b
    elif operator == "subtract":
        result = a - b
    return result


res = solve(input(), int(input()), int(input()))
print(res)
