cards_given = input().split(" ")
team_A = []
team_B = []
game_was_terminated = False
#team generator
for index in range(1, 12):
    team_A.append(f"A-{index}")
    team_B.append(f"B-{index}")

#iterating through the card list and the teams
for player in cards_given:
    if player in team_A:
        team_A.remove(player)
    elif player in team_B:
        team_B.remove(player)

    if len(team_A) < 7 or len(team_B) < 7:
        game_was_terminated = True
        break

print(f"Team A - {len(team_A)}; Team B - {len(team_B)}")

if game_was_terminated:
    print("Game was terminated")