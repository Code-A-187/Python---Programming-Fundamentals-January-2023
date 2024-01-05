# Input
price_by_product = {}
quantity_by_product = {}

# Logic
while True:
    line = input()
    if line == "buy":
        break

    args = line.split()
    product = args[0]
    price = float(args[1])
    quantity = int(args[2])

    price_by_product[product] = price
    if product in price_by_product:
        quantity_by_product[product] += quantity
    else:
        quantity_by_product[product] = quantity

# Output
for product in price_by_product:
    price = price_by_product[product]
    quantity = quantity_by_product[product]
    total_price = price * quantity

    print(f"{product} -> {total_price:.2f}")
