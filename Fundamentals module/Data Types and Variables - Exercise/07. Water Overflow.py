water_tank_capacity = 255
total_liters_poured = 0
count = int(input())

for iteration in range(count):
    liters_poured = int(input())
    total_liters_poured += liters_poured
    if water_tank_capacity < total_liters_poured:
        print("Insufficient capacity!")
        total_liters_poured -= liters_poured
print(total_liters_poured)