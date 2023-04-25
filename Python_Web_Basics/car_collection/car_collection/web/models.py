from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from car_collection.web.validators import YearBetweenValidator


class Profile(models.Model):
    USERNAME_MAX_LENGTH = 10
    USERNAME_MIN_LENGTH = 2
    USER_NAME_VALIDATION_ERROR = f"The username must be a minimum of {USERNAME_MIN_LENGTH} chars"
    AGE_MIN_VALUE = 18
    PASSWORD_MAX_LENGTH = 30
    FIRST_NAME_MAX_LENGTH = 30
    LAST_NAME_MAX_LENGTH = 30

    username = models.CharField(max_length=USERNAME_MAX_LENGTH,
                                validators=(MinLengthValidator(USERNAME_MIN_LENGTH, USER_NAME_VALIDATION_ERROR),))
    email = models.EmailField()
    age = models.PositiveIntegerField(validators=(MinValueValidator(AGE_MIN_VALUE),))
    password = models.CharField(max_length=PASSWORD_MAX_LENGTH)
    first_name = models.CharField(max_length=FIRST_NAME_MAX_LENGTH, blank=True)
    last_name = models.CharField(max_length=LAST_NAME_MAX_LENGTH, blank=True)
    profile_picture = models.URLField(blank=True)

    def __str__(self):
        return f"[{self.id}] {self.username}"

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

class Car(models.Model):
    TYPE_MAX_LENGTH = 10
    MODEL_MAX_LENGTH = 20
    MODEL_MIN_LENGTH = 2
    PRICE_MIN_VALUE = 1
    MIN_YEAR = 1980
    MAX_YEAR = 2049

    SPORTS_CAR = "Sports Car"
    PICKUP = "Pickup"
    CROSSOVER = "Crossover"
    MINIBUS = "Minibus"
    OTHER = "Other"

    CAR_TYPE_CHOICES = (
        (SPORTS_CAR, "Sports Car"),
        (PICKUP, "Pickup"),
        (CROSSOVER, "Crossover"),
        (MINIBUS, "Minibus"),
        (OTHER, "Other"),
    )

    type = models.CharField(max_length=TYPE_MAX_LENGTH, choices=CAR_TYPE_CHOICES)
    model = models.CharField(max_length=MODEL_MAX_LENGTH, validators=(MinLengthValidator(MODEL_MIN_LENGTH),))
    year = models.PositiveIntegerField(validators=(YearBetweenValidator(MIN_YEAR, MAX_YEAR),))
    image_url = models.URLField(verbose_name="Image URL")
    price = models.FloatField(validators=(MinValueValidator(PRICE_MIN_VALUE),))


    def __str__(self):
        return f"[{self.id}] - {self.model}"
