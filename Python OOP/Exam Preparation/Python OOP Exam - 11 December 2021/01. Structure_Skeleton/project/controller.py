from project.car.muscle_car import MuscleCar
from project.car.sports_car import SportsCar
from project.driver import Driver
from project.race import Race


class Controller:
    def __init__(self):
        self.cars = []
        self.drivers = []
        self.races = []

    def create_car(self, car_type: str, model: str, speed_limit: int):
        if model in [car.model for car in self.cars]:
            raise Exception(f"Car {model} is already created!")

        if car_type == "MuscleCar" or car_type == "SportsCar":
            self.cars.append(eval(car_type)(model, speed_limit))
            return f"{car_type} {model} is created."

    def create_driver(self, driver_name: str):
        if driver_name in [driver.name for driver in self.drivers]:
            raise Exception(f"Driver {driver_name} is already created!")

        self.drivers.append(Driver(driver_name))
        return f"Driver {driver_name} is created."

    def create_race(self, race_name: str):
        if race_name in [race.name for race in self.races]:
            raise Exception(f"Race {race_name} is already created!")

        self.races.append(Race(race_name))
        return f"Race {race_name} is created."

    def add_car_to_driver(self, driver_name, car_type):
        if driver_name not in [driver.name for driver in self.drivers]:
            raise Exception(f"Driver {driver_name} could not be found!")
        if car_type not in ("SportsCar", "MuscleCar"):
            raise Exception(f"Car {car_type} could not be found!")
        available_cars = [car for car in self.cars if car.__class__.__name__ == car_type and car.is_taken is False]

        driver = [driver for driver in self.drivers if driver.name == driver_name][0]
        if len(available_cars) == 0:
            raise Exception(f"Car {car_type} could not be found!")
        car_to_add = available_cars[-1]
        if driver.car:
            driver_old_car = driver.car
            driver_old_car.is_taken = False
            driver.car = car_to_add
            car_to_add.is_taken = True
            return f"Driver {driver.name} changed his car from {driver_old_car.model} to {driver.car.model}."
        driver.car = car_to_add
        car_to_add.is_taken = True
        return f"Driver {driver_name} chose the car {driver.car.model}."

    def add_driver_to_race(self, race_name, driver_name):
        if race_name not in [race.name for race in self.races]:
            raise Exception(f"Race {race_name} could not be found!")
        if driver_name not in [driver.name for driver in self.drivers]:
            raise Exception(f"Driver {driver_name} could not be found!")
        driver = [driver for driver in self.drivers if driver.name == driver_name][0]
        race = [race for race in self.races if race.name == race_name][0]
        if driver.car is None:
            raise Exception(f"Driver {driver_name} could not participate in the race!")
        if driver in race.drivers:
            raise Exception(f"Driver {driver_name} is already added in {race_name} race.")
        race.drivers.append(driver)
        return f"Driver {driver_name} added in {race_name} race."

    def start_race(self, race_name):
        if race_name not in [race.name for race in self.races]:
            raise Exception(f"Race {race_name} could not be found!")
        race = [race for race in self.races if race.name == race_name][0]
        if len(race.drivers) < 3:
            raise Exception(f"Race {race_name} cannot start with less than 3 participants!")
        winner_speeds = sorted([driver.car.speed_limit for driver in race.drivers], reverse=True)[:3]
        result = ''
        for speed in winner_speeds:
            driver = [driver for driver in race.drivers if driver.car.speed_limit == speed][0]
            result += f"Driver {driver.name} wins the {race_name} race with a speed of {driver.car.speed_limit}." + '\n'
            driver.number_of_wins += 1

        return result.strip()