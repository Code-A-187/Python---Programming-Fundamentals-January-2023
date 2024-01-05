
customer = input()
computer_price = 0

special_price = False
while True:
    if customer == 'special':
        special_price = True
        break
    elif customer == 'regular':
        break
    else:
        price = float(customer)
        if price < 0:
            print('Invalid price!')
        else:
            computer_price += price
    customer = input()

taxes = computer_price * 0.2
total_price = computer_price + taxes

if special_price:
    total_price *= 0.9
if computer_price == 0:
    print('Invalid order!')
else:
    print(f"Congratulations you've just bought a new computer!\n"
          f"Price without taxes: {computer_price:.2f}$\n"
          f"Taxes: {taxes:.2f}$\n"
          f"-----------\n"
          f"Total price: {total_price:.2f}$")
