from collections import deque

males = [int(num) for num in input().split()]
females = deque([int(num) for num in input().split()])
total_matches = 0

while True:
    if not males or not females:
        break

    last_male = males[-1]
    first_female = females[0]

    if first_female <= 0 or last_male <= 0:
        if first_female <= 0:
            females.popleft()
        if last_male <= 0:
            males.pop()
        continue

    if last_male % 25 == 0 or first_female % 25 == 0:
        if last_male % 25 == 0:
            males.pop()
            males.pop()
        if first_female % 25 == 0:
            females.popleft()
            females.popleft()
        continue

    if first_female == last_male:
        females.popleft()
        males.pop()
        total_matches += 1
        continue
    else:
        females.popleft()
        males[-1] -= 2

print(f"Matches: {total_matches}")
if males:
    males.reverse()
    print(f'Males left: ', end='')
    print(', '.join([str(m) for m in males]))
else:
    print('Males left: none')

if females:
    print('Females left: ', end='')
    print(', '.join([str(f) for f in females]))
else:
    print('Females left: none')