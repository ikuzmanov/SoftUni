# Generated by Django 4.1.5 on 2023-01-10 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("web", "0005_nullblankdemo"),
    ]

    operations = [
        migrations.AddField(
            model_name="employee",
            name="works_full_time",
            field=models.BooleanField(null=True),
        ),
    ]
