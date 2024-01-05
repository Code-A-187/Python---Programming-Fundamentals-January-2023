integers_list = [int(x) for x in input().split()]

data = input()

while data != 'end':
    command_args = data.split()
    command = command_args[0]
    if command == 'swap':
        index_one = int(command_args[1])
        index_two = int(command_args[2])
        integers_list[index_one], integers_list[index_two] = integers_list[index_two], integers_list[index_one]
    elif command == 'multiply':
        index_one = int(command_args[1])
        index_two = int(command_args[2])
        integers_list[index_one] = integers_list[index_one] * integers_list[index_two]
    elif command == 'decrease':
        for i in range(len(integers_list)):
            integers_list[i] -= 1

    data = input()

print(', '.join(map(str, integers_list)))
