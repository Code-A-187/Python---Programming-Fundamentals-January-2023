digits = input().split(', ')

for number in digits:
    if number == number[::-1]:
        is_palindrome = True
    else:
        is_palindrome = False

    print(is_palindrome)
