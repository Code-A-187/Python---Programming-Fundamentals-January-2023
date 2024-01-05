data = input()

cities = {}

while data != 'Sail':
    splitted_data = data.split('||')
    city = splitted_data[0]
    population = int(splitted_data[1])
    gold = int(splitted_data[2])
    if city not in cities:
        cities[city] = {'population': population, 'gold': gold}
    else:
        cities[city]['population'] += population
        cities[city]['gold'] += gold

    data = input()

data = input()

while data != 'End':
    spllited_data = data.split('=>')
    command = spllited_data[0]
    city = spllited_data[1]
    if command == 'Plunder':
        people = int(spllited_data[2])
        gold = int(spllited_data[3])

        cities[city]['population'] -= people
        cities[city]['gold'] -= gold
        print(f'{city} plundered! {gold} gold stolen, {people} citizens killed.')

        if cities[city]['population'] <= 0 or cities[city]['gold'] <= 0:
            del[cities[city]]
            print(f"{city} has been wiped off the map!")

    elif command == 'Prosper':
        gold = int(spllited_data[2])
        if gold >= 0:
            cities[city]['gold'] += gold
            print(f"{gold} gold added to the city treasury. {city} now has {cities[city]['gold']} gold.")
        else:
            print(f'Gold added cannot be a negative number!')

    data = input()
if not cities:
    print('Ahoy, Captain! All targets have been plundered and destroyed!')
else:
    print(f'Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:')
    for city, value in cities.items():
        print(f'{city} -> Population: {cities[city]["population"]} citizens, Gold: {cities[city]["gold"]} kg')
