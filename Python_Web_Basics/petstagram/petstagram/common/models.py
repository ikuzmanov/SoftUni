from django.db import models

from petstagram.photos.models import Photo


# Create your models here.
class PhotoComment(models.Model):
    MAX_TEXT_LENGTH = 300
    text = models.CharField(max_length=MAX_TEXT_LENGTH, null=False, blank=False)
    publication_date_and_time = models.DateTimeField(auto_now_add=True, blank=True, null=False)
    photo = models.ForeignKey(Photo, on_delete=models.RESTRICT, null=False, blank=True)


class PhotoLike(models.Model):
    # Photo's field for likes is name {NAME_OF_THIS_MODEL}_set
    photo = models.ForeignKey(Photo, on_delete=models.RESTRICT, blank=True, null=False)
