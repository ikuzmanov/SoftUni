count_of_commands = int(input())

license_numbers = set()

for _ in range(count_of_commands):
    direction, car_number = input().split(", ")
    if direction == "IN":
        license_numbers.add(car_number)

    elif direction == "OUT":
        license_numbers.remove(car_number)

if license_numbers:
    print(*license_numbers, sep="\n")
else:
    print("Parking Lot is Empty")


