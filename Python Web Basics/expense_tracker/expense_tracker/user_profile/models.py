from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from expense_tracker.core.validators import raise_if_not_letters, validate_file_less_than_5MB
from django.templatetags.static import static


# Create your models here.
class UserProfile(models.Model):
    NAME_MAX_LENGTH = 15
    NAME_MIN_LENGTH = 2

    first_name = models.CharField(
        max_length=NAME_MAX_LENGTH,
        validators=(MinLengthValidator(NAME_MIN_LENGTH), raise_if_not_letters)
    )

    last_name = models.CharField(
        max_length=NAME_MAX_LENGTH,
        validators=(MinLengthValidator(NAME_MIN_LENGTH), raise_if_not_letters)
    )

    budget = models.DecimalField(default=0, validators=(MinValueValidator(0),), max_digits=5,
                                 decimal_places=2)

    profile_image = models.ImageField(
        upload_to='profile_images/',
        blank=True,
        null=True,
        validators=(validate_file_less_than_5MB,),

    )

    def __str__(self):
        return f"[{self.id}] {self.first_name} {self.last_name}"
