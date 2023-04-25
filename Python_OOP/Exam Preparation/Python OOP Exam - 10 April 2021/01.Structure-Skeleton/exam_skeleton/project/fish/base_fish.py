from abc import ABC, abstractmethod

from project.validator import Validator


class BaseFish(ABC):
    @abstractmethod
    def __init__(self, name: str, species: str, size: int, price: float):
        self.name = name
        self.species = species
        self.size = size
        self.price = price

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.raise_if_string_is_empty(value, "Fish name")
        self.__name = value

    @property
    def species(self):
        return self.__species

    @species.setter
    def species(self, value):
        Validator.raise_if_string_is_empty(value, "Fish species")
        self.__species = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        Validator.raise_if_price_is_equal_or_below_zero(value, "Price")
        self.__price = value

    @abstractmethod
    def eat(self):
        self.size += 5
