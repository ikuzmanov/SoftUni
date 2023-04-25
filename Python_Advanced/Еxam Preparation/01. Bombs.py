from collections import deque

bomb_effects = deque(int(num) for num in input().split(", "))
bomb_casing = [int(num) for num in input().split(", ")]

recipes = {
    40: 'Datura Bombs',
    60: 'Cherry Bombs',
    120: 'Smoke Decoy Bombs',
}

pouch = {
    'Cherry Bombs': 0,
    'Datura Bombs': 0,
    'Smoke Decoy Bombs': 0,
}

while bomb_effects and bomb_casing:
    if all(value >= 3 for value in pouch.values()):
        break

    effect = bomb_effects[0]
    casing = bomb_casing[-1]

    if not effect + casing in recipes.keys():
        bomb_casing[-1] -= 5
    else:
        pouch[recipes[effect + casing]] += 1
        bomb_effects.popleft()
        bomb_casing.pop()

if all(value >= 3 for value in pouch.values()):
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")

if bomb_effects:
    print(f"Bomb Effects: {', '.join([str(x) for x in bomb_effects])}")
else:
    print("Bomb Effects: empty")

if bomb_casing:
    print(f"Bomb Casings: {', '.join([str(x) for x in bomb_casing])}")
else:
    print("Bomb Casings: empty")

sorted_pouch = sorted(pouch.items(), key = lambda kv: kv[0])

for item, value in sorted_pouch:
    print(f"{item}: {value}")
