import re

pattern = r"^>>(?P<furniture>[a-zA-Z]+)<<(?P<price>\d+\.?\d*)!(?P<quantity>\d+)$"

total_sum = 0
command = input()

bought_furniture = []

while command != "Purchase":
    match = re.search(pattern, command)
    if match:
        furniture, price, quantity = match.groups()
        bought_furniture.append(furniture)
        total_sum += int(quantity) * float(price)
    command = input()

print("Bought furniture: ")
for furniture in bought_furniture:
    print(furniture)
print(f"Total money spend: {total_sum:.2f}")