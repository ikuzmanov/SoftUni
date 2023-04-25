class Catalogue:
    products = []

    def __init__(self, name: str):
        self.name = name

    def add_product(self, product: str):
        Catalogue.products.append(product)

    def get_by_letter(self, letter: str):
        filtered_list = [product for product in Catalogue.products if product[0] == letter]
        return filtered_list

    def __repr__(self):
        catalogue_list = "\n".join(sorted(Catalogue.products))
        return f"Items in the {self.name} catalogue:\n{catalogue_list}"


catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)
