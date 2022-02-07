guests_count = int(input())

vip_list = set()
regular_list = set()

for _ in range(guests_count):
    reservation_code = input()
    if reservation_code[0].isdigit() and len(reservation_code) == 8:
        vip_list.add(reservation_code)
    elif len(reservation_code) == 8:
        regular_list.add(reservation_code)

guest_code = input()
while not guest_code == "END":
    if guest_code in vip_list:
        vip_list.remove(guest_code)
    elif guest_code in regular_list:
        regular_list.remove(guest_code)

    guest_code = input()
sorted_vip_list = sorted(vip_list)
sorted_regular_list = sorted(regular_list)

print(len(sorted_vip_list) + len(sorted_regular_list))
print(*sorted_vip_list, sep="\n")
print(*sorted_regular_list, sep="\n")