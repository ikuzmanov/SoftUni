def is_inside(row, col):
    return 0 <= row < dartboard and 0 <= col < dartboard


def corresponding_nums(row, col, matrix):
    result = int(matrix[row][0]) + int(matrix[row][-1]) + int(matrix[0][col]) + int(matrix[-1][col])
    return result


class Players:
    def __init__(self, name, points, throws):
        self.name = name
        self.points = points
        self.throws = throws
        self.is_winner = False

    def winner(self):
        self.is_winner = True


first_player_name, second_player_name = input().split(', ')
dartboard = 7
matrix = []

first_player = Players(first_player_name, 501, 0)
second_player = Players(second_player_name, 501, 0)
player_turn = 1

for rows in range(dartboard):
    matrix.append(input().split())

while True:
    throw_row, throw_col = eval(input())

    if player_turn % 2 != 0:
        player = first_player
    else:
        player = second_player

    player.throws += 1
    if not is_inside(throw_row, throw_col):
        player_turn += 1
        continue

    if matrix[throw_row][throw_col].isdigit():
        player.points -= int(matrix[throw_row][throw_col])
    elif matrix[throw_row][throw_col] == 'D':
        player.points -= corresponding_nums(throw_row, throw_col, matrix) * 2
    elif matrix[throw_row][throw_col] == 'T':
        player.points -= corresponding_nums(throw_row, throw_col, matrix) * 3

    if player.points <= 0 or matrix[throw_row][throw_col] == "B":
        player.winner()
        break

    player_turn += 1

if first_player.is_winner:
    print(f"{first_player.name} won the game with {first_player.throws} throws!")
else:
    print(f"{second_player.name} won the game with {second_player.throws} throws!")
