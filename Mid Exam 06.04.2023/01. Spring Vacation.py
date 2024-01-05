travel_days = int(input())
budget = float(input())
people = int(input())
fuel_price = float(input())
food_day_price = float(input())
room_day_price = float(input())

budget_needed = 0

all_food_expenses = food_day_price * travel_days * people
all_room_expenses = room_day_price * travel_days * people
if people > 10:
    all_room_expenses *= 0.75

budget_needed += all_food_expenses + all_room_expenses

for day in range(1, travel_days + 1):
    kilometer = int(input())
    fuel_expenses = fuel_price * kilometer
    budget_needed += fuel_expenses
    if day % 3 == 0:
        budget_needed *= 1.4
    if day % 5 == 0:
        budget_needed *= 1.4
    if day % 7 == 0:
        received_money = budget_needed / people
        budget_needed -= received_money

if budget > budget_needed:
    print(f'You have reached the destination. You have {(budget - budget_needed):.2f}$ budget left.')
else:
    print(f'Not enough money to continue the trip. You need {(budget_needed - budget):.2f}$ more.')
