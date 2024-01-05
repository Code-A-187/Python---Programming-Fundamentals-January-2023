def calculate_total_price(product, quantity):
    total_amount = 0
    if product == "coffee":
        total_amount = quantity * 1.50
    elif product == "coke":
        total_amount = quantity * 1.40
    elif product == "water":
        total_amount = quantity * 1.00
    elif product == "snacks":
        total_amount = quantity * 2.00
    return total_amount


product_type = input()
quantity_purchased = int(input())

result = (calculate_total_price(product_type, quantity_purchased))
print(f'{result:.2f}')
