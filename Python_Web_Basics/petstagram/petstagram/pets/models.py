from django.db import models
from django.template.defaultfilters import slugify

from petstagram.core.model_mixin import StrFromFieldsMixin


# Create your models here.


class Pet(StrFromFieldsMixin, models.Model):
    str_fields = ('id', 'name')
    MAX_NAME = 30
    name = models.CharField(max_length=MAX_NAME, null=False, blank=False)
    personal_photo = models.URLField(null=False, blank=False)
    date_of_birth = models.DateField(null=True, blank=True)
    slug = models.SlugField(null=False, blank=True, unique=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.slug:
            self.slug = slugify(f"{self.id}-{self.name}")
        return super().save(*args, **kwargs)

