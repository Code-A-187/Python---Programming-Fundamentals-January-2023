lines = int(input())

plants = {}

for _ in range(lines):
    plants_args = input().split('<->')
    plant = plants_args[0]
    rarity = int(plants_args[1])
    if plant not in plants:
        plants[plant] = {'rarity': rarity, 'rating': []}
    else:
        plants[plant]['rarity'] = rarity
        plants[plant]['rating'] = []

data = input()

while data != 'Exhibition':
    splitted_data = data.split(': ')
    command = splitted_data[0]
    if command == 'Rate':
        values = splitted_data[1].split(' - ')
        plant = values[0]
        rating = int(values[1])
        if plant in plants:
            plants[plant]['rating'].append(rating)
        else:
            print('error')
    elif command == 'Update':
        values = splitted_data[1].split(' - ')
        plant = values[0]
        new_rarity = int(values[1])
        if plant in plants:
            plants[plant]['rarity'] = new_rarity
        else:
            print('error')
    elif command == 'Reset':
        plant = splitted_data[1]
        if plant in plants:
            plants[plant]['rating'] = []
        else:
            print('error')

    data = input()

print(f'Plants for the exhibition:')
for plant, value in plants.items():
    average_rating = 0
    if not plants[plant]['rating']:
        average_rating = 0
    else:
        average_rating = sum(plants[plant]['rating']) / len(plants[plant]['rating'])
    print(f"- {plant}; Rarity: {plants[plant]['rarity']}; Rating: {average_rating:.2f}")
