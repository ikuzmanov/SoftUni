from abc import ABC

from project.food import Food

food_to_eat = {
    "Mice": ("vegetable", 'fruit'),
    "Hen": ('vegetable', 'meat', 'seed', 'fruit'),
    "Cat": ('vegetable', 'meat'),
    'Tiger': ('meat',),
    'Dog': ('meat',),
    'Owl': ('meat',),
}

all_sounds = {
    "Owl": "Hoot Hoot",
    "Hen": "Cluck",
    "Mouse": "Squeak",
    "Dog": "Woof!",
    "Cat": "Meow",
    "Tiger": "ROAR!!!"
}

food_weight = {
    'Hen': 0.35,
    'Owl': 0.25,
    'Mouse': 0.10,
    'Cat': 0.30,
    'Dog': 0.40,
    'Tiger': 1.00,
}


class Animal(ABC):
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.food_eaten = 0

    def make_sound(self):
        return all_sounds[self.__class__.__name__]

    def feed(self, food: Food):
        food_name = food.__class__.__name__.lower()
        animal_name = self.__class__.__name__

        if food_name not in food_to_eat[animal_name]:
            return f"{animal_name} does not eat {food.__class__.__name__}!"

        self.food_eaten += food.quantity
        self.weight += food_weight[animal_name] * food.quantity


class Bird(Animal, ABC):
    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight)
        self.wing_size = wing_size

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.wing_size}, {self.weight}, {self.food_eaten}]"


class Mammal(Animal, ABC):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight)
        self.living_region = living_region

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"
