fires_with_their_cells=input().split("#")
water=int(input())
number_scope=[]
total_fire=0
effort=0
for elements in fires_with_their_cells:
    separate_elements=elements.split(" = ")
    level=separate_elements[0]
    scope=int(separate_elements[1])
    if level=="Low" and 1<=scope<=50 and water>=scope:
        water-=scope
        total_fire+=scope
        number_scope.append(str(scope))
    elif level == "Medium" and 51 <= scope <=80 and water>=scope:
        water -= scope
        total_fire += scope
        number_scope.append(str(scope))
    elif level == "High" and 81 <= scope <= 125 and water>=scope:
        water -= scope
        total_fire += scope
        number_scope.append(str(scope))
    effort = total_fire * 0.25
 
print("Cells:")
for i in number_scope:
    print(f"{'-'} {i}")
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")