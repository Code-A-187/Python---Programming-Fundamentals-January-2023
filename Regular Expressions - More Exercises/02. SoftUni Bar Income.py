import re

pattern = r'\%(?P<customer>[A-Z][a-z]+)\%[^\|\$\%\.]*?\<(?P<product>\w+)\>[^\|\$\%\.]*?\|(?P<count>[0-9]+)\|[\w\-]*?(?P<price>[0-9.]+[0-9])(?=\$)'

text = input()


total_income = 0
while text != 'end of shift':
    sells = re.finditer(pattern, text)
    # извличане на информация от групуте в текста регистрирани от регекса
    for info in sells:
        sell_data = info.groupdict()
        day_income = int(sell_data['count']) * float(sell_data['price'])
        total_income += day_income
        print(f"{sell_data['customer']}: {sell_data['product']} - {day_income:.2f}")

    text = input()

print(f'Total income: {total_income:.2f}')
