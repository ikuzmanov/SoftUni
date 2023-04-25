neighborhood = [int(num) for num in input().split("@")]
command = input()
current_index = 0
count = 0

while not command == "Love!":
    current_command, length = command.split()
    current_index += int(length)
    if current_index >= len(neighborhood):
        current_index = 0
    for house in range(len(neighborhood)):
        if house == current_index:
            if not neighborhood[house] == 0:
                neighborhood[house] -= 2
                if neighborhood[house] == 0:
                    print(f"Place {house} has Valentine's day.")
            elif neighborhood[house] == 0:
                print(f"Place {house} already had Valentine's day.")

    command = input()

print(f"Cupid's last position was {current_index}.")

res = all(ele == 0 for ele in neighborhood)
if res:
    print("Mission successful")
else:
    fails = 0
    for failed in neighborhood:
        if failed >= 1:
            fails += 1
    print(f"Cupid has failed {fails} places.")
