# Generated by Django 4.1.5 on 2023-01-18 19:14

from django.db import migrations, models
import petstagram.photos.models


class Migration(migrations.Migration):

    dependencies = [
        ("photos", "0003_alter_photo_tagged_pets"),
    ]

    operations = [
        migrations.AlterField(
            model_name="photo",
            name="photo",
            field=models.ImageField(
                blank=True,
                upload_to="mediafiles/pet_photos/",
                validators=[petstagram.photos.models.validate_file_less_than_5MB],
            ),
        ),
    ]
