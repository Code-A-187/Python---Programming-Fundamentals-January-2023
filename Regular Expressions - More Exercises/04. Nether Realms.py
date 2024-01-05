import re

demons = re.split(", *", input())

demons_book = {}

demon_health_pattern = r'[^\d\+\-*\/\.]'
demon_damage_pattern = r'(?:\+|-)?[0-9]+(?:\.[0-9]+)?'
demon_operators_pattern = r'[*\/]'

for demon in demons:
    demon = demon.strip() # махаме празните места пред и зад текста
    # сумираме ASCII на всички букви намерени в името на демона и ги слагаме в лист към дневника
    demons_book[demon] = [sum([ord(x) for x in re.findall(demon_health_pattern, demon)])]

    demon_damage = re.finditer(demon_damage_pattern, demon)
    operators = re.findall(demon_operators_pattern, demon)
    current_demon_damage = 0

    for value in demon_damage:
        # вадим стойностите от регекса превръщаме ги в реални числа и прибавяме към демиджа
        current_demon_damage += float(value.group(0))

    for operator in operators:
        if operator == '*':
            current_demon_damage *= 2
        elif operator == '/':
            current_demon_damage /= 2

    demons_book[demon].append(current_demon_damage)

for demon, stats in sorted(demons_book.items()):
    print(f"{demon} - {stats[0]} health, {stats[1]:.2f} damage")
