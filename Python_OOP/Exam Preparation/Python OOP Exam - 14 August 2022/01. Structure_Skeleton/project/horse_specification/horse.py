from abc import ABC, abstractmethod

from project.core.validator import Validator


class Horse(ABC):
    @abstractmethod
    def __init__(self, name: str, speed: int):
        self.name = name
        self.speed = speed
        self.is_taken = False


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.raise_if_less_than_limit(value, 4, f"Horse name {value} is less than 4 symbols!")
        self.__name = value

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, value):
        Validator.raise_if_horse_speed_is_greater_than(value, self.speed_limit, "Horse speed is too high!")
        self.__speed = value

    def train(self):
        if self.speed + self.train_value_increase > self.speed_limit:
            self.speed = self.speed_limit
        else:
            self.speed += self.train_value_increase
