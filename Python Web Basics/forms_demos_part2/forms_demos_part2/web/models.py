from django.db import models

from forms_demos_part2.web.validators import validate_text, ValueInRangeValidator


# Create your models here.
class Todo(models.Model):
    MAX_LEN_TEXT = 25
    text = models.CharField(max_length=MAX_LEN_TEXT, null=False, blank=False, validators=(validate_text,))
    priority = models.IntegerField(validators=(ValueInRangeValidator,), null=False, blank=False, )
    is_done = models.BooleanField(null=False, blank=False, default=False)
