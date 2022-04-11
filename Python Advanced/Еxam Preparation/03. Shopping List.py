def shopping_list(budget, **kwargs):
    if budget < 100:
        return "You do not have enough budget."

    products = []
    basket = set()

    for product, price_and_quantity in kwargs.items():
        if len(basket) >= 5:
            break
        price, quantity = price_and_quantity
        total_sum = price*quantity

        if budget >= total_sum:
            products.append(f"You bought {product} for {total_sum:.2f} leva.")
            basket.add(product)
            budget -= total_sum

    return "\n".join(products)


print(shopping_list(104,
                    cola=(1.20, 2),
                    candies=(0.25, 15),
                    bread=(1.80, 1),
                    pie=(10.50, 5),
                    tomatoes=(4.20, 1),
                    milk=(2.50, 2),
                    juice=(2, 3),
                    eggs=(3, 1),
                    ))
