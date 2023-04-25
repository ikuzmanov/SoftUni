from project.product import Product


class ProductRepository:
    def __init__(self):
        self.products = []

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name: str):
        for rep_product in self.products:
            if rep_product.name == product_name:
                return rep_product

    def remove(self, product_name):
        product = self.find(product_name)
        if product is not None:
            self.products.remove(product)

    def __repr__(self):
        result = ""
        for rep_product in self.products:
            result += f"{rep_product.name}: {rep_product.quantity}\n"

        return result.strip()
