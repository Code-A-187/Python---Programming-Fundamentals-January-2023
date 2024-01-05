# Input

orders = int(input())

total = 0

# Logic
for _ in range(orders):
    capsule_price = float(input())
    days = int(input())
    coffee_per_day = int(input())

    if capsule_price < 0.01 or capsule_price > 100.00:
        continue
    if days < 1 or days > 31:
        continue
    if coffee_per_day < 1 or coffee_per_day > 2000:
        continue

    order_price = capsule_price * (days * coffee_per_day)
    total += order_price

    print(f"The price for the coffee is: ${order_price:.2f}")

# Output

print(f"Total: ${total:.2f}")
