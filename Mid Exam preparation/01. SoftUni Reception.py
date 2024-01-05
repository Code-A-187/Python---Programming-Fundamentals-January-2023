employee_one, employee_two, employee_three = int(input()), int(input()), int(input())

students_count = int(input())

answers_per_hour = employee_one + employee_two + employee_three
time = 0
for hour in range(1, students_count):
    if students_count <= 0:
        break
    time += 1
    if hour % 4 == 0:
        continue
    else:
        students_count -= answers_per_hour
print(f'Time needed: {time}h.')
