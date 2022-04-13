# size = 8
# matrix = []
#
# king_row = 0
# king_col = 0
# total_queens = 0
# queens_found = []
# for row in range(size):
#     row_elements = (input().split())
#     matrix.append(row_elements)
#
#     for col in range(size):
#         if row_elements[col] == "K":
#             king_col, king_row = col, row
#         if row_elements[col] == "Q":
#             total_queens += 1
#
#
# def queen_is_found_up(king_col, king_row, matrix):
#     for row in range(king_row, -1, -1):
#         if matrix[row][king_col] == "Q":
#             return [row, king_col]
#     return False
#
# def queen_is_found_right(king_col, king_row, matrix):
#     for col in range(king_col, size, 1):
#         if matrix[king_row][col] == "Q":
#             return [king_row, col]
#     return False
#
# def queen_is_found_down(king_col, king_row, matrix):
#     for row in range(king_row, size, 1):
#         if matrix[row][king_col] == "Q":
#             return [row, king_col]
#     return False
#
# def queen_is_found_left(king_col, king_row, matrix):
#     for col in range(king_col, -1, -1):
#         if matrix[king_row][col] == "Q":
#             return [king_row, col]
#     return False
#
# def queen_is_found_up_left_diagonal(king_col, king_row, matrix):
#     for row in range(king_row-1, -1, -1):
#         king_col -= 1
#         if matrix[row][king_col] == "Q":
#             return [row, king_col]
#     return False
#
# def queen_is_found_up_right_diagonal(king_col, king_row, matrix):
#     for row in range(king_row+1, size, 1):
#         king_col += 1
#         if matrix[row][king_col] == "Q":
#             return [row, king_col]
#     return False
#
# def queen_is_found_down_right_diagonal(king_col, king_row, matrix):
#     for row in range(king_row-1, -1, -1):
#         king_col += 1
#         if matrix[row][king_col] == "Q":
#             return [row, king_col]
#     return False
#
# def queen_is_found_down_left_diagonal(king_col, king_row, matrix):
#     for row in range(king_row+1, size, 1):
#         king_col -= 1
#         if matrix[row][king_col] == "Q":
#             return [row, king_col]
#     return False
#
# for _ in range(1):
#     try:
#         result = queen_is_found_up(king_col, king_row, matrix)
#         if result:
#             queens_found.append(result)
#
#         result = queen_is_found_right(king_col, king_row, matrix)
#         if result:
#             queens_found.append(result)
#
#         result = queen_is_found_down(king_col, king_row, matrix)
#         if result:
#             queens_found.append(result)
#
#         result = queen_is_found_left(king_col, king_row, matrix)
#         if result:
#             queens_found.append(result)
#
#         result = queen_is_found_up_left_diagonal(king_col, king_row, matrix)
#         if result:
#             queens_found.append(result)
#
#         result = queen_is_found_up_right_diagonal(king_col, king_row, matrix)
#         if result:
#             queens_found.append(result)
#
#         result = queen_is_found_down_right_diagonal(king_col, king_row, matrix)
#         if result:
#             queens_found.append(result)
#         result = queen_is_found_down_left_diagonal(king_col, king_row, matrix)
#         if result:
#             queens_found.append(result)
#     except IndexError:
#         continue
# if queens_found:
#
#     print(*queens_found, sep = "\n")
#
# else:
#     print("The king is safe")


def is_queen(i_x, i_y):
    for j in range(1, 9):
        current_x = k_x - j * i_x
        current_y = k_y - j * i_y
        if not (0 <= current_x < 8 and 0 <= current_y < 8):
            break
        if board[current_x][current_y] == 'Q':
            result.append([current_x, current_y])
            break


board = []
k_x = 0
k_y = 0
result = []

for i in range(8):
    board.append(input().split())
    if 'K' in board[i]:
        k_x = i
        k_y = board[i].index('K')

for x in range(-1, 2):
    for y in range(-1, 2):
        is_queen(x, y)

if result:
    for c in result:
        print(c)
else:
    print('The king is safe!')