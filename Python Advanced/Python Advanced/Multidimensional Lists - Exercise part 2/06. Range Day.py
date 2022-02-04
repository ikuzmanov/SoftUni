matrix = [[x for x in input().split()] for _ in range(5)]
my_x, my_y = 0, 0
targets_count = 0
shotted_targets = []
for row in range(5):
    for col in range(len(matrix[row])):
        if matrix[row][col] == 'A':
            my_x, my_y = row, col
        elif matrix[row][col] == 'x':
            targets_count += 1
number_of_commands = int(input())
for _ in range(number_of_commands):
    command_arg = input().split()
    command, side = command_arg[0], command_arg[1]
    if command_arg[0] == 'move':
        steps = int(command_arg[2])
        if steps < 1:
            continue
        else:
            next_x, next_y = my_x, my_y
            if side == 'right':
                next_y += steps
            elif side == 'left':
                next_y -= steps
            elif side == 'up':
                next_x -= steps
            elif side == 'down':
                next_x += steps
            if 0 <= next_x < 5 and 0 <= next_y < 5 and (not matrix[next_x][next_y] == 'x'):
                my_x, my_y = next_x, next_y
    else:
        is_target = False
        target_x, target_y = my_x, my_y
        if side == 'right':
            for col in range(my_y, 5):
                if matrix[my_x][col] == 'x':
                    target_y = col
                    is_target = True
                    break
        elif side == 'left':
            for col in range(my_y, -1, -1):
                if matrix[my_x][col] == 'x':
                    target_y = col
                    is_target = True
                    break
        elif side == 'up':
            for row in range(my_x, -1, -1):
                if matrix[row][my_y] == 'x':
                    target_x = row
                    is_target = True
                    break
        elif side == 'down':
            for row in range(my_x, 5):
                if matrix[row][my_y] == 'x':
                    target_x = row
                    is_target = True
                    break
        if is_target:
            targets_count -= 1
            shotted_targets.append([target_x, target_y])
            matrix[target_x][target_y] = '.'
        if targets_count < 1:
            break
if targets_count > 0:
    print(f'Training not completed! {targets_count} targets left.')
else:
    print(f'Training completed! All {len(shotted_targets)} targets hit.')
[print(target) for target in shotted_targets]