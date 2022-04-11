from collections import deque

crafted_gifts = []


def crafting(combined):
    if 100 <= combined <= 199:
        return "Gemstone"
    elif 200 <= combined <= 299:
        return "Porcelain Sculpture"
    elif 300 <= combined <= 399:
        return "Gold"
    elif 400 <= combined <= 499:
        return "Diamond Jewellery"


crafting_materials = [int(num) for num in input().split()]
genie_magic_level = deque(int(num) for num in input().split())

while True:
    if not crafting_materials or not genie_magic_level:
        break
    material = crafting_materials[-1]
    magic_level = genie_magic_level[0]
    combined = material + magic_level
    result = crafting(combined)
    if result:
        crafted_gifts.append(result)
        crafting_materials.pop()
        genie_magic_level.popleft()
        continue
    else:
        if combined < 100 and combined % 2 == 0:
            combined = (material * 2) + (magic_level * 3)
            result = crafting(combined)
            if result:
                crafted_gifts.append(result)
                crafting_materials.pop()
                genie_magic_level.popleft()
                continue
        elif combined < 100 and combined % 2 != 0:
            combined = (material * 2) + (magic_level * 2)
            result = crafting(combined)
            if result:
                crafted_gifts.append(result)
                crafting_materials.pop()
                genie_magic_level.popleft()
                continue
        elif combined > 499:
            combined = combined / 2
            result = crafting(combined)
            if result:
                crafted_gifts.append(result)
                crafting_materials.pop()
                genie_magic_level.popleft()
                continue
        crafting_materials.pop()
        genie_magic_level.popleft()

if "Gemstone" in crafted_gifts and "Porcelain Sculpture" in crafted_gifts \
        or "Gold" in crafted_gifts and "Diamond Jewellery" in crafted_gifts:
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")

if crafting_materials:
    print(f"Materials left: {', '.join(str(x) for x in crafting_materials)}")
if genie_magic_level:
    print(f"Magic left: {', '.join(str(x) for x in genie_magic_level)}")

sorted_gift_list = sorted(set(crafted_gifts))
for gift in sorted_gift_list:
    print(f"{gift}: {crafted_gifts.count(gift)}")