number_of_dragons = int(input())
dragons_by_colours = {}

for _ in range(number_of_dragons):
    colour, name, damage, health, armor = input().split()
    if colour not in dragons_by_colours:
        dragons_by_colours[colour] = {}
    if damage == "null":
        dragon_damage = 45
    else:
        dragon_damage = int(damage)
    if health == "null":
        dragon_health = 250
    else:
        dragon_health = int(health)
    if armor == "null":
        dragon_armor = 10
    else:
        dragon_armor = int(armor)
    dragons_by_colours[colour][name] = [dragon_damage, dragon_health, dragon_armor]

average_per_colour = {}
for colour, name in dragons_by_colours.items():
    avg_for_colour = []
    for dragon, info in name.items():
        if len(name) > 1:
            avg_for_colour.append(info)
        else:
            avg_for_colour.append(info)
        avg_result = [sum(i) / len(avg_for_colour) for i in zip(*avg_for_colour)]
    average_per_colour[colour] = avg_result

sorted_dictionary = {k: {x: y for x, y in sorted(v.items())} for k, v in dragons_by_colours.items()}

for colour, average in average_per_colour.items():
    print(f"{colour}::({average[0]:.2f}/{average[1]:.2f}/{average[2]:.2f})")
    for name, info in sorted_dictionary[colour].items():
        print(f"-{name} -> damage: {info[0]}, health: {info[1]}, armor: {info[2]}")

print(dragons_by_colours)
print(average_per_colour)