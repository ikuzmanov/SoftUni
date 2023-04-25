from django.db import models

from forms_demos_part2.web.validators import validate_text, ValueInRangeValidator


class Person(models.Model):
    MAX_LEN_NAME = 20

    name = models.CharField(max_length=MAX_LEN_NAME)
    profile_image = models.ImageField(upload_to='persons', null=True, blank=True)

    def __str__(self):
        return self.name


# Create your models here.
class Todo(models.Model):
    MAX_LEN_TEXT = 25
    MAX_TODOS_COUNT_PER_PERSON = 3

    text = models.CharField(max_length=MAX_LEN_TEXT, null=False, blank=False, validators=(validate_text,))
    priority = models.IntegerField(validators=(ValueInRangeValidator(1, 10),), null=False, blank=False, )
    is_done = models.BooleanField(null=False, blank=False, default=False)
    assignee = models.ForeignKey(Person, on_delete=models.RESTRICT)
