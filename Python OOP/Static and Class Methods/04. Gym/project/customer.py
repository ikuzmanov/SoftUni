class Customer:
    id = 0

    def __init__(self, name: str, address: str, email: str):
        self.name = name
        self.address = address
        self.email = email
        self.id = self.get_next_id()

    @classmethod
    def get_next_id(cls):
        Customer.id += 1
        return Customer.id


    def __repr__(self):
        return f"Customer <{self.id}> {self.name}; Address: {self.address}; Email: {self.email}"

Gosho = Customer("Georgi", "ivaylo 57", "on4e@gmail.com")
Pesho = Customer("Petar", "neofit rilski 57", "on4e@abv.com")
a=5