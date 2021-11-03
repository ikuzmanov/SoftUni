class Vehicle:
    def __init__(self, type, model, price):
        self.type = type
        self.model = model
        self.price = price
        self.owner = None

    def buy(self, money: int, owner: str):
        if self.owner is not None:
            return 'Car already sold'
        else:
            if money >= self.price:
                self.owner = owner
                return f'Successfully bought a {self.type}. Change: {money - self.price:.2f}'
            return'Sorry, not enough money'

    def sell(self):
        if self.owner is not None:
            self.owner = None
        else:
            return 'Vehicle has no owner'

    def __repr__(self):
        if self.owner is None:
            return f'{self.model} {self.type} is on sale: {self.price}'
        return f'{self.model} {self.type} is owned by: {self.owner}'

vehicle_type = "car"
model = "BMW"
price = 30000
vehicle = Vehicle(vehicle_type, model, price)
vehicle.buy(15000, "Peter")
vehicle.buy(35000, "George")
print(vehicle)
vehicle.sell()
print(vehicle)

