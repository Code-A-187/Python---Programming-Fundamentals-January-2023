number = int(input())

is_prime = True

for i in range(2, 9 + 1):
    if number % i == 0:
        is_prime = False
    else:
        is_prime = True

    if is_prime == False:
        break

print(is_prime)
