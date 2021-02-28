# TEAM GENERATOR
# for num in range(1, 12):
#     print(f"\"A-{num}\"", end=", ")
#     print(f"\"B-{num}\"", end=", ")

# if len(team_a) < 7 or len(team_b) < 7:
#     print(f'Team A - {team_a}; Team B - {team_b}')
#     print('Game was terminated')


red_cards = input().split()

team_a = ["A-1", "A-2", "A-3", "A-4", "A-5", "A-6", "A-7", "A-8", "A-9", "A-10", "A-11"]
team_b = ["B-1", "B-2", "B-3", "B-4", "B-5", "B-6", "B-7", "B-8", "B-9", "B-10", "B-11"]
sent_off_a = []
sent_off_b = []

for player in red_cards:
    if len(team_a) < 7 or len(team_b) < 7:
        break
    else:
        if 'A' in player:
            if player in sent_off_a:
                continue
            sent_off_a.append(player)
            team_a.remove(player)
        elif 'B' in player:
            if player in sent_off_b:
                continue
            sent_off_b.append(player)
            team_b.remove(player)

if len(team_a) < 7 or len(team_b) < 7:
    print(f'Team A - {len(team_a)}; Team B - {len(team_b)}')
    print('Game was terminated')
else:
    print(f'Team A - {len(team_a)}; Team B - {len(team_b)}')
