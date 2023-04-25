data = input()

products = {}

while data != "buy":
    name, price, quantity = data.split()
    if name not in products:
        products[name] = []
        products[name].append(float(price))
        products[name].append(float(quantity))
    else:
        products[name][0] = float(price)
        products[name][1] += float(quantity)
    data = input()

for name, price_quantity in products.items():
    total_cost = price_quantity[0] * price_quantity[1]
    print(f"{name} -> {total_cost:.2f}")