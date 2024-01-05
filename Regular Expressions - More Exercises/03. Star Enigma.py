import re

msg_count = int(input())
pattern = r'\@(?P<planet>[A-Z][a-z]*)[^\@\-\!\:\>]*?\:(?P<population>[0-9]+)[^\@\-\!\:\>]*?\!(?P<action>[A|D])\![^\@\-\!\:\>]*?\->(?P<soldiers>[0-9]+)'

attacked_count = 0
attacked_planets = []
destroyed_count = 0
destroyed_planets = []

for _ in range(msg_count):
    message = input()
    count = len(re.findall(r's|t|a|r', message.lower()))
    encryted_message = ''.join(map(chr, [ord(x) - count for x in message]))
    # извличане на информация от групите в текста регистрирани от регекса
    data = re.finditer(pattern, encryted_message)
    for info in data:
        planet_data = info.groupdict()
        if planet_data['action'] == 'A':
            attacked_count += 1
            attacked_planets.append(planet_data['planet'])
        else:
            destroyed_count += 1
            destroyed_planets.append(planet_data['planet'])

print(f'Attacked planets: {attacked_count}')
if len(attacked_planets) > 0:
    for el in sorted(attacked_planets):
        print(f"-> {el}")
print(f'Destroyed planets: {destroyed_count}')
if len(destroyed_planets) > 0:
    for el in sorted(destroyed_planets):
        print(f"-> {el}")
