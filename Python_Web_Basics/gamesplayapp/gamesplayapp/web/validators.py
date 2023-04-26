from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class RatingBetweenValues:
    def __init__(self, min_rating, max_rating):
        self.min_rating = min_rating
        self.max_rating = max_rating

    def __call__(self, value):
        if value < self.min_rating or value > self.max_rating:
            raise ValidationError(self.__get_exception_message())

    def __get_exception_message(self):
        return f"Rating must be between {self.min_rating} and {self.max_rating}"
