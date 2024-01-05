#Input

cards = input().split()

team_a_count = 0
team_b_count = 0

players_a_list = []
players_b_list = []

should_terminate = False
for card in cards:
    card_args = card.split("-")
    team_name = card_args[0]
    player_number = card_args[1]
    if team_name == "A":
        if player_number in players_a_list:
            continue
        else:
            team_a_count += 1
            players_a_list.append(player_number)
    else:
        if player_number in players_b_list:
            continue
        else:
            team_b_count += 1
            players_b_list.append(player_number)
    if len(players_a_list) > 4 or len(players_b_list) > 4:
        should_terminate = True
        break

# Output

print(f"Team A - {11 - team_a_count}; Team B - {11 - team_b_count}")

if team_a_count > 4 or team_b_count > 4:
    print("Game was terminated")
