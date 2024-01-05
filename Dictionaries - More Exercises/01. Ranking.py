line = input()

pass_for_contest = {}

while line != 'end of contests':
    contest_args = line.split(':')
    contest = contest_args[0]
    password = contest_args[1]
    pass_for_contest[contest] = password
    line = input()

data = input()
final_dict = {}

while data != 'end of submissions':
    result_args = data.split('=>')
    contest = result_args[0]
    password = result_args[1]
    name = result_args[2]
    result = int(result_args[3])
    if contest in pass_for_contest and password in pass_for_contest[contest]:
        if name not in final_dict:
            final_dict[name] = {contest: result}
        else:
            if contest not in final_dict[name]:
                final_dict[name][contest] = result
            else:
                if result > final_dict[name][contest]:
                    final_dict[name][contest] = result
    data = input()

max_points = 0
name = ''

for user, info in final_dict.items():
    total_points = 0
    for contest, number in info.items():
        total_points += number
    if total_points >= max_points:
        max_points = total_points
        name = user

print(f'Best candidate is {name} with total {max_points} points.')

sorted_dictionary = sorted(final_dict.items(), key=lambda x: x[0])

print(f'Ranking:')

for name, info in sorted_dictionary:
    print(f'{name}')

    sorted_contest = sorted(info.items(), key=lambda x: -x[1])
    for contest, result in sorted_contest:
        print(f'#  {contest} -> {result}')
