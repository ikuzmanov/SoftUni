# Generated by Django 4.1.5 on 2023-01-13 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("web", "0014_employee_years_of_experience_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="employee",
            name="email",
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
