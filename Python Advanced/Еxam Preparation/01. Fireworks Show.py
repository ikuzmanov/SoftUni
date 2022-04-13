from collections import deque


firework_effects = deque([int(num) for num in input().split(", ") if int(num) > 0])
explosive_power = [int(num) for num in input().split(", ") if int(num) > 0]

crafted_fireworks = {
    "Palm Fireworks": 0,
    "Willow Fireworks": 0,
    "Crossette Fireworks": 0,
}
show_ready = False
a = 5
while True:
    firework_show = [True if num >= 3 else False for num in crafted_fireworks.values()]
    if all(firework_show):
        show_ready = True
        break

    if len(firework_effects) == 0 or len(explosive_power) == 0:
        break

    effect_to_mix = firework_effects[0]
    explosive_to_mix = explosive_power[-1]
    combo = effect_to_mix + explosive_to_mix

    if combo % 3 == 0 and combo % 5 != 0:
        crafted_fireworks["Palm Fireworks"] += 1
        firework_effects.popleft()
        explosive_power.pop()

    elif combo % 5 == 0 and combo % 3 != 0:
        crafted_fireworks["Willow Fireworks"] += 1
        firework_effects.popleft()
        explosive_power.pop()

    elif combo % 5 == 0 and combo % 3 == 0:
        crafted_fireworks["Crossette Fireworks"] += 1
        firework_effects.popleft()
        explosive_power.pop()

    else:
        effect_to_mix = firework_effects.popleft()
        effect_to_mix -= 1
        firework_effects.append(effect_to_mix)

if show_ready:
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can't make the perfect firework show.")

if firework_effects:
    print(f"Firework Effects left: {', '.join(str(num) for num in firework_effects)}")

if explosive_power:
    print(f"Explosive Power left: {', '.join(str(num) for num in explosive_power)}")

for key,value in crafted_fireworks.items():
    print(f"{key}: {value}")
