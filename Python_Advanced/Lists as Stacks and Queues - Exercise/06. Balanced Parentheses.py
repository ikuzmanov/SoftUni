expression = input()

opening_brackets = []

balanced = True

for character in expression:
    if character in "({[":
        opening_brackets.append(character)
    elif not opening_brackets:
        balanced = False
        break
    else:
        last_opening_bracket = opening_brackets.pop()
        if f"{last_opening_bracket}{character}" not in '()[]{}':
            balanced = False
            break

if balanced and not opening_brackets:
    print("YES")
else:
    print("NO")