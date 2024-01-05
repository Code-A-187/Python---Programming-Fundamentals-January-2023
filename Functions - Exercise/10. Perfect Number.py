def is_perfect_number(num):
    sm = 0
    for i in range(1, num):
        if num % i == 0:
            sm = sm + i
    return sm


number = int(input())

if is_perfect_number(number) == number:
    print(f"We have a perfect number!")
else:
    print(f"It's not so perfect.")

