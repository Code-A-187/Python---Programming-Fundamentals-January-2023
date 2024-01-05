
data = input()

animals_dict = {}
areas = {}

while data != 'EndDay':
    command_args = data.split(': ')
    command = command_args[0]
    animal_args = command_args[1].split('-')
    animal_name = animal_args[0]
    if command == 'Add':
        food_needed = int(animal_args[1])
        area = animal_args[2]
        if area not in areas:
            areas[area] = 0
        if animal_name in animals_dict:
            animals_dict[animal_name]['food'] += food_needed
        else:
            animals_dict[animal_name] = {'food': food_needed, 'area': area}
            areas[area] += 1

    elif command == 'Feed':
        food_given = int(animal_args[1])
        if animal_name in animals_dict:
            animals_dict[animal_name]['food'] -= food_given
            if animals_dict[animal_name]['food'] <= 0:
                print(f'{animal_name} was successfully fed')
                area = animals_dict[animal_name]['area']
                areas[area] -= 1
                del animals_dict[animal_name]
    data = input()

print('Animals:')
for animal in animals_dict:
    animal_food = animals_dict[animal]['food']
    print(f' {animal} -> {animal_food}g')

print('Areas with hungry animals:')
for area in areas:
    if areas[area] > 0:
        print(f'{area}: {areas[area]}')

