from datetime import date

from django.core.exceptions import ValidationError


def validate_before_today(value):
    if value > date.today():
        raise ValidationError(f'{value} is in the future')