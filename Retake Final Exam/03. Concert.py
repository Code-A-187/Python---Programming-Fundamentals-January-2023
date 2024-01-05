data = input()

bands_list = {}
bands_time = {}
total_time = 0
first_band_is_in = False
while data != 'Start!':
    command_args = data.split('; ')
    command = command_args[0]
    band_name = command_args[1]
    if command == 'Add':
        band_members = command_args[2].split(', ')
        if band_name not in bands_list:
                bands_list[band_name] = band_members
        elif band_name in bands_list:
            for member in band_members:
                if member not in bands_list[band_name]:
                    bands_list[band_name].append(member)
    elif command == 'Play':
        play_time = int(command_args[2])
        total_time += play_time
        if band_name not in bands_time:
            bands_time[band_name] = play_time
        else:
            bands_time[band_name] += play_time
    data = input()
print(f'Total time: {total_time}')
for band_name in bands_time.items():
    print(f'{band_name[0]} -> {band_name[1]}')
first_band = next(iter(bands_time))
for bandName, members in bands_list.items():
    if bandName == first_band:
        print(f'{bandName}')
        for member in members:
            print(f'=> {member}')
