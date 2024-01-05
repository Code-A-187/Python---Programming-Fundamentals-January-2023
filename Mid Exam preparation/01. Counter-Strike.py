energy = int(input())

win_count = 0

while True:
    distance = input()
    if distance == 'End of battle':
        print(f'Won battles: {win_count}. Energy left: {energy}')
        break
    else:
        if int(distance) > energy:
            print(f'Not enough energy! Game ends with {win_count} won battles and {energy} energy')
            break
        else:
            energy -= int(distance)
            win_count += 1
    if win_count % 3 == 0:
        energy += win_count
