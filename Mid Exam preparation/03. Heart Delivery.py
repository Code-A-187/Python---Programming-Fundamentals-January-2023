houses_list = [int(x) for x in input().split('@')]

data = input()
last_position = 0

while data != 'Love!':
    command_args = data.split()
    jump = command_args[0]
    length = int(command_args[1])
    last_position += length
    if last_position >= len(houses_list):
        if houses_list[0] <= 0:
            print(f"Place {houses_list.index(houses_list[0])} already had Valentine's day.")
        else:
            houses_list[0] -= 2
            if houses_list[0] <= 0:
                print(f"Place {houses_list.index(houses_list[0])} has Valentine's day.")
        last_position = 0
    else:
        if houses_list[last_position] <= 0:
            print(f"Place {last_position} already had Valentine's day.")
        else:
            houses_list[last_position] -= 2
            if houses_list[last_position] <= 0:
                print(f"Place {last_position} has Valentine's day.")
    data = input()

print(f"Cupid's last position was {last_position}.")

success = 0

for house in houses_list:
    if house > 0:
        success += 1

if success > 0:
    print(f'Cupid has failed {success} places.')
else:
    print('Mission was successful.')
