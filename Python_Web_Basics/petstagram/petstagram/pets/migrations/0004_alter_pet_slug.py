# Generated by Django 4.1.5 on 2023-01-18 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pets", "0003_pet_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="pet",
            name="slug",
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
