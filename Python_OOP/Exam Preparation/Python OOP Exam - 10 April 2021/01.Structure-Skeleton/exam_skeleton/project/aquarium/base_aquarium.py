from abc import ABC, abstractmethod

from project.validator import Validator


class BaseAquarium(ABC):
    @abstractmethod
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.decorations = []
        self.fish = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.raise_if_string_is_empty(value, "Aquarium name")
        self.__name = value

    def calculate_comfort(self):
        return sum([decor.comfort for decor in self.decorations])

    def add_fish(self, fish):
        fish_types = ("FreshwaterFish", "SaltwaterFish")
        current_aquarium_size = self.capacity - sum([fish.size for fish in self.fish])
        if current_aquarium_size - fish.size < 0:
            return "Not enough capacity."
        if fish.__class__.__name__ in fish_types:
            self.fish.append(fish)
            return f"Successfully added {fish.__class__.__name__} to {self.name}."

    def remove_fish(self, fish):
        self.fish.remove(fish)

    def add_decoration(self, decoration):
        self.decorations.append(decoration)

    def feed(self):
        for fish in self.fish:
            fish.eat()

    def __str__(self):
        result = f"{self.name}:\nFish: "
        if len(self.fish) == 0:
            result += "none"
        else:
            for fish in self.fish:
                result += f"{fish.name} "

        result += f"\nDecorations: {len(self.decorations)}\nComfort: {self.calculate_comfort()}\n"
        return result