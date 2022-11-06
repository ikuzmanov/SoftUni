from abc import ABC, abstractmethod

from project.core.validator import Validator
from project.user import User


class Movie(ABC):
    @abstractmethod
    def __init__(self, title: str, year: int, owner: object, age_restriction: int):
        self.title = title
        self.year = year
        self.owner = owner
        self.age_restriction = age_restriction
        self.likes = 0

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        Validator.raise_if_string_is_empty(value, "The title cannot be empty string!")
        self.__title = value

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, value):
        Validator.raise_if_num_is_below_limit(1888, value, "Movies weren't made before 1888!")
        self.__year = value

    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, user: User):
        Validator.raise_if_not_object_type("User", user, "The owner must be an object of type User!")
        self.__owner = user

    def details(self):
        return f"{self.__class__.__name__} - Title:{self.title}, Year:{self.year}, Age restriction:{self.age_restriction}, Likes:{self.likes}, Owned by:{self.owner.username}"

    @property
    def age_restriction(self):
        return self.__age_restriction

    @age_restriction.setter
    def age_restriction(self, value):
        Validator.raise_if_num_is_below_limit(self.limit, value,
                                              f"{self.__class__.__name__} movies must be restricted for audience under {self.limit} years!")
        self.__age_restriction = value
