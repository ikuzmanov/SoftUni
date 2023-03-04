from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class YearBetweenValidator:
    def __init__(self, min_year, max_year):
        self.min_year = min_year
        self.max_year = max_year

    def __call__(self, value):
        if value < self.min_year or value > self.max_year:
            raise ValidationError(self.__get_exception_message())

    def __get_exception_message(self):
        return f"Year must be between {self.min_year} and {self.max_year}"
