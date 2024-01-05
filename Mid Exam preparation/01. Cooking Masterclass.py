from math import ceil
# Input
budget = float(input())
students = int(input())


flour_price = float(input())
egg_price = (float(input()) * 10) * students
apron_price = float(input()) * ceil(students * 1.2)

flour_price_needed = 0

# Logic

for i in range(1, students + 1):
    flour_price_needed += flour_price
    if i % 5 == 0:
        flour_price_needed -= flour_price


money_needed = flour_price_needed + egg_price + apron_price

# Output

if money_needed <= budget:
    print(f"Items purchased for {money_needed:.2f}$.")
else:
    print(f"{money_needed - budget:.2f}$ more needed.")
