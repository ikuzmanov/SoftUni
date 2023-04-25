companions = int(input())
days = int(input())
total_coins = 0

for day in range(1, days + 1):
    if day % 10 == 0:
        companions -= 2
    if day % 15 == 0:
        companions += 5
    if day % 3 == 0:
        total_coins -= 3 * companions
    if day % 5 == 0:
        total_coins += 20 * companions
        if day % 3 == 0:
            total_coins -= 2 * companions
    total_coins += 50
    total_coins -= companions * 2

coins_per_companion = int(total_coins/companions)
print(f"{companions} companions received {coins_per_companion} coins each.")
