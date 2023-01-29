# Generated by Django 4.1.5 on 2023-01-18 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pets", "0004_alter_pet_slug"),
        ("photos", "0002_create_photo"),
    ]

    operations = [
        migrations.AlterField(
            model_name="photo",
            name="tagged_pets",
            field=models.ManyToManyField(blank=True, to="pets.pet"),
        ),
    ]