from project.aquarium.base_aquarium import BaseAquarium
from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.aquarium.saltwater_aquarium import SaltwaterAquarium
from project.controller import Controller
from project.decoration.decoration_repository import DecorationRepository
from project.decoration.ornament import Ornament
from project.decoration.plant import Plant
from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish

controller = Controller()
print(controller.add_aquarium("FreshwaterAquarium", "aquarium1"))
print(controller.add_aquarium("SaltwaterAquarium", "aquarium2"))
print(controller.add_aquarium("SaltwaterAquarium1", "aquarium2"))
print(controller.add_decoration("Ornament"))
print(controller.add_decoration("Plant"))
print(controller.add_decoration("Plant1"))
print(controller.insert_decoration("aquarium1", "Ornament"))
print(controller.insert_decoration("aquarium1", "Plant"))
print(controller.insert_decoration("aquarium1", "Plant"))
print(controller.add_fish("aquarium1", "FreshwaterFish", "fish1", "specie1", 5))
print(controller.add_fish("aquarium1", "FreshwaterFish", "fish2", "specie2", 10))
print(controller.feed_fish("aquarium1"))
print(controller.calculate_value("aquarium1"))
print(controller.report())
a=5
# print(controller.__dict__)