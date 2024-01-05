line = input()

user_position_points = {}

while line != 'Season end':
    to_delete = None
    lose_skill = None
    if '->' in line:
        statistic_args = line.split(' -> ')
        username = statistic_args[0]
        position = statistic_args[1]
        points = int(statistic_args[2])

        if username not in user_position_points:
            user_position_points[username] = {position: points}
        elif username in user_position_points and position not in user_position_points[username]:
            user_position_points[username].update({position: points})
        elif username in user_position_points and position in user_position_points[username] \
                and points > user_position_points[username][position]:
            user_position_points[username][position] = points
    elif 'vs' in line:
        players_args = line.split(' vs ')
        player_1 = players_args[0]
        player_2 = players_args[1]

        if player_1 in user_position_points and player_2 in user_position_points:
            for position_1 in user_position_points[player_1]:
                for position_2 in user_position_points[player_2]:
                    if position_1 == position_2:
                        if user_position_points[player_1][position_1] == user_position_points[player_2][position_2]:
                            break
                        elif user_position_points[player_1][position_1] > user_position_points[player_2][position_2]:
                            to_delete = player_2
                            lose_skill = position_1
                            break
                        elif user_position_points[player_1][position_1] < user_position_points[player_2][position_2]:
                            to_delete = player_1
                            lose_skill = player_2
                            break
            if to_delete is not None:
                del user_position_points[to_delete][lose_skill]
                to_delete = None
                lose_skill = None
            break
    line = input()
for player, info in sorted(user_position_points.items(), key=lambda x: (-sum(i for i in x[1].values()), x[0])):
    if len(user_position_points[player]) == 0:
        continue
    else:
        print(f"{player}: {sum(info.values())} skill")
    for position, points in sorted(user_position_points[player].items(), key=lambda x: (-x[1], x[0])):
        print(f' - {position} <::> {points}')