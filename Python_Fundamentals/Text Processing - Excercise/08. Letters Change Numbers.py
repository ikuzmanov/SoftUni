seq = input().split()
total = 0

for s in seq:
    fletter = s[0]
    sletter = s[-1]
    fcode = ord(fletter.lower()) - 96
    scode = ord(sletter.lower()) - 96

    number = int(s[1:-1])
    if fletter.islower(): current = number * fcode
    else: current = number / fcode

    if sletter.islower(): current = current + scode
    else: current = current - scode

    total += current

print(f"{total:.2f}")
