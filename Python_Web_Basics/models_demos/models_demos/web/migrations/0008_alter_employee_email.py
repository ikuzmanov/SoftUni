# Generated by Django 4.1.5 on 2023-01-10 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("web", "0007_employee_level_alter_employee_works_full_time"),
    ]

    operations = [
        migrations.AlterField(
            model_name="employee",
            name="email",
            field=models.EmailField(editable=False, max_length=254, unique=True),
        ),
    ]