# Generated by Django 4.1.5 on 2023-01-16 11:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("web", "0016_alter_employee_options_department_created_on_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="category",
            options={"verbose_name_plural": "Categories"},
        ),
    ]