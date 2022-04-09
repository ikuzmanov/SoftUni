from project.astronaut.astronaut_repository import AstronautRepository
from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.astronaut.meteorologist import Meteorologist
from project.planet.planet import Planet
from project.planet.planet_repository import PlanetRepository


class SpaceStation:
    def __init__(self):
        self.planet_repository = PlanetRepository()
        self.astronaut_repository = AstronautRepository()
        self.number_of_not_completed_missions = 0
        self.number_of_successful_missions = 0

    def add_astronaut(self, astronaut_type: str, name: str):
        astronaut = self.astronaut_repository.find_by_name(name)
        valid_astronauts = {
            "Biologist": Biologist,
            "Geodesist": Geodesist,
            "Meteorologist": Meteorologist,
        }
        if astronaut:
            return f"{astronaut.name} is already added."

        if astronaut_type not in valid_astronauts:
            raise Exception("Astronaut type is not valid!")

        self.astronaut_repository.add(valid_astronauts[astronaut_type](name))
        return f"Successfully added {astronaut_type}: {name}."

    def add_planet(self, name: str, items: str):
        planet = self.planet_repository.find_by_name(name)
        items = items.split(", ")
        if planet:
            return f"{name} is already added."
        planet = Planet(name)
        planet.items += items
        self.planet_repository.add(planet)

    def retire_astronaut(self, name: str):
        astronaut = self.astronaut_repository.find_by_name(name)
        if astronaut is None:
            raise Exception(f"Astronaut {name} doesn't exist!")
        self.astronaut_repository.remove(astronaut)
        return f"Astronaut {name} was retired!"

    def recharge_oxygen(self):
        for astronaut in self.astronaut_repository.astronauts:
            astronaut.oxygen += 10

    def send_on_mission(self, planet_name: str):
        planet_to_explore = self.planet_repository.find_by_name(planet_name)
        if planet_to_explore is None:
            raise Exception("Invalid planet name!")
        sorted_astronauts = list(sorted(self.astronaut_repository.astronauts, key=lambda x: -x.oxygen))
        suitable_astronauts = [astr for astr in sorted_astronauts if astr.oxygen > 30][:5]
        if not suitable_astronauts:
            raise Exception("You need at least one astronaut to explore the planet!")

        astros_went_to_open_space = []
        for astr in suitable_astronauts:
            while True:
                if planet_to_explore.items:
                    astr.backpack.append(planet_to_explore.items.pop())
                    astr.breathe()
                    if astr not in astros_went_to_open_space:
                        astros_went_to_open_space.append(astr)
                    if astr.oxygen <= 0:
                        break
                else:
                    break
        if planet_to_explore.items:
            self.number_of_not_completed_missions += 1
            return "Mission is not completed."
        self.number_of_successful_missions += 1
        return f"Planet: {planet_name} was explored. {len(astros_went_to_open_space)} astronauts participated in collecting items."

    def report(self):
        result = f"{self.number_of_successful_missions} successful missions!\n" \
                 f"{self.number_of_not_completed_missions} missions were not completed!\n" \
                 f"Astronauts' info:\n"
        for astr in self.astronaut_repository.astronauts:
            backpack_data = ', '.join(astr.backpack) if astr.backpack else "none"
            result += f"Name: {astr.name}\n"
            result += f"Oxygen: {astr.oxygen}\n"
            result += f"Backpack items: {backpack_data}\n"
            return result.strip()
