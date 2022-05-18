room_count = int(input())

all_chairs = 0
all_visitors = 0

for room_number in range(1, room_count+1):
    total_chairs, visitors = input().split()
    total_chairs = len(total_chairs)
    visitors = int(visitors)
    difference = visitors - total_chairs
    all_chairs += total_chairs
    all_visitors += visitors

    if total_chairs < visitors:
        print(f"{difference} more chairs needed in room {room_number}")


if all_chairs >= all_visitors:
    difference = all_chairs - all_visitors
    print(f"Game On, {abs(difference)} free chairs left")





