from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from expense_tracker.core.validators import raise_if_not_letters, MaxFileSizeInMbValidator


class UserProfile(models.Model):
    NAME_MAX_LENGTH = 15
    NAME_MIN_LENGTH = 2

    BUDGET_MIN_VALUE = 0
    BUDGET_DEFAULT_VALUE = 0

    IMAGE_UPLOAD_DIR = 'profile_images/'
    IMAGE_MAX_SIZE_IN_MB = 5

    first_name = models.CharField(
        max_length=NAME_MAX_LENGTH,
        validators=(MinLengthValidator(NAME_MIN_LENGTH), raise_if_not_letters)
    )

    last_name = models.CharField(
        max_length=NAME_MAX_LENGTH,
        validators=(MinLengthValidator(NAME_MIN_LENGTH), raise_if_not_letters)
    )

    budget = models.DecimalField(default=BUDGET_DEFAULT_VALUE, validators=(MinValueValidator(BUDGET_MIN_VALUE),),
                                 max_digits=8,
                                 decimal_places=2)

    profile_image = models.ImageField(
        upload_to=IMAGE_UPLOAD_DIR,
        blank=True,
        null=True,
        validators=(MaxFileSizeInMbValidator(IMAGE_MAX_SIZE_IN_MB),),
    )

    def __str__(self):
        return f"[{self.id}] {self.first_name} {self.last_name}"
