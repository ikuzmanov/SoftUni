def calculate_price(product, price):
    if product == "coffee":
        return 1.5 * price
    if product == "water":
        return 1.0 * price
    if product == "coke":
        return 1.40 * price
    if product == "snacks":
        return 2.0 * price


product = input()
price = float(input())

res = calculate_price(product, price)

print(f"{res:.2f}")
