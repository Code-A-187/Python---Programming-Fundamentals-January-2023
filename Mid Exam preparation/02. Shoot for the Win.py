targets_list = [int(x) for x in input().split()]


shot_target = 0
while True:
    end = input()
    if end == 'End':
        print(f'Shot targets: {shot_target} -> {" ".join(map(str, targets_list))}')
        break
    index = int(end)
    if index in range(len(targets_list)):
        target_value = targets_list[index]
        for i in range(len(targets_list)):
            if targets_list[i] > 0:
                if targets_list[i] > target_value:
                    targets_list[i] -= target_value
                else:
                    targets_list[i] += target_value
        targets_list[index] = -1
        shot_target += 1
