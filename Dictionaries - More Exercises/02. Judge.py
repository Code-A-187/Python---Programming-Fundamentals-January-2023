line = input()

contest_points_by_user, user_points_by_contest = {}, {}

while line != 'no more time':
    statistic_args = line.split(' -> ')
    username = statistic_args[0]
    contest = statistic_args[1]
    points = int(statistic_args[2])

    if contest not in contest_points_by_user:
        contest_points_by_user[contest] = {username: points}
    if username not in contest_points_by_user[contest]:
        contest_points_by_user[contest][username] = points
    if username not in user_points_by_contest:
        user_points_by_contest[username] = {contest: points}
    else:
        user_points_by_contest[username][contest] = points
    if contest_points_by_user[contest][username] < points:
        contest_points_by_user[contest][username] = points
    if user_points_by_contest[username][contest] < points:
        user_points_by_contest[username][contest] = points
    line = input()

for contest, username in contest_points_by_user.items():
    i = 1
    print(f'{contest}: {len(username)} participants')
    sorted_items = sorted(username.items(), key=lambda x: (-x[1], x[0]))
    for user, points in sorted_items:
        print(f'{i}. {user} <::> {points}')
        i += 1

print('Individual standings:')
sorted_names = sorted(user_points_by_contest.items(), key=lambda x: (-sum(x[1].values()), x[0]))
i = 1
for user, points in sorted_names:
    print(f'{i}. {user} -> {sum(points.values())}')
    i += 1
