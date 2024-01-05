from math import ceil
students = int(input())
lectures = int(input())
add_bonus = int(input())

max_bonus = 0
student_attend = 0

for i in range(students):
    attend = int(input())
    total_bonus = attend / lectures * (5 + add_bonus)
    if total_bonus > max_bonus:
        max_bonus = total_bonus
        student_attend = attend

print(f"Max Bonus: {ceil(max_bonus)}.")
print(f"The student has attended {student_attend} lectures.")
