numbers_as_str = input().split()
rounded_numbers = []

for num_as_str in numbers_as_str:
    rounded_numbers.append(round(float(num_as_str)))

print(rounded_numbers)
