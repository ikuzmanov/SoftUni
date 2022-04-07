from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.aquarium.saltwater_aquarium import SaltwaterAquarium
from project.decoration.decoration_repository import DecorationRepository
from project.decoration.ornament import Ornament
from project.decoration.plant import Plant
from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish


class Controller:
    def __init__(self):
        self.decorations_repository = DecorationRepository()
        self.aquariums = []

    def add_aquarium(self, aquarium_type: str, aquarium_name: str):
        valid_aquariums = ("FreshwaterAquarium", "SaltwaterAquarium")
        if aquarium_type not in valid_aquariums:
            return "Invalid aquarium type."
        self.aquariums.append(eval(aquarium_type)(aquarium_name))
        return f"Successfully added {aquarium_type}."

    def add_decoration(self, decoration_type: str):
        if decoration_type not in ("Ornament", "Plant"):
            return "Invalid decoration type."
        decoration = eval(decoration_type)()
        self.decorations_repository.add(decoration)
        return f"Successfully added {decoration_type}."

    def insert_decoration(self, aquarium_name: str, decoration_type: str):
        decoration = self.get_decoration_by_type(decoration_type)
        aquarium = self.get_aquarium_by_name(aquarium_name)

        if not decoration:
            return f"There isn't a decoration of type {decoration_type}."

        if aquarium:
            aquarium.add_decoration(decoration)
            self.decorations_repository.remove(decoration)
            return f"Successfully added {decoration_type} to {aquarium_name}."

    def add_fish(self, aquarium_name: str, fish_type: str, fish_name: str, fish_species: str, price: float):
        aquarium = self.get_aquarium_by_name(aquarium_name)
        if fish_type not in ("FreshwaterFish", "SaltwaterFish"):
            return f"There isn't a fish of type {fish_type}."
        fish = eval(fish_type)(fish_name, fish_species, price)
        if fish.__class__.__name__[:-4] == aquarium.__class__.__name__[:-8]:
            return aquarium.add_fish(fish)
        return "Water not suitable."

    def feed_fish(self, aquarium_name: str):
        aquarium = self.get_aquarium_by_name(aquarium_name)
        aquarium.feed()
        return f"Fish fed: {len(aquarium.fish)}"

    def calculate_value(self, aquarium_name: str):
        aquarium = self.get_aquarium_by_name(aquarium_name)
        fish_cost = sum([fish.price for fish in aquarium.fish])
        decorations_cost = sum([decoration.price for decoration in aquarium.decorations])
        return f"The value of Aquarium {aquarium.name} is {fish_cost + decorations_cost:.2f}."

    def report(self):
        result = ""
        for aquarium in self.aquariums:
            result += str(aquarium)
        return result

    def get_decoration_by_type(self, decoration_type):
        for decoration in self.decorations_repository.decorations:
            if decoration.__class__.__name__ == decoration_type:
                return decoration
        return None

    def get_aquarium_by_name(self, aquarium_name: str):
        for aquarium in self.aquariums:
            if aquarium_name == aquarium.name:
                return aquarium
        return None

