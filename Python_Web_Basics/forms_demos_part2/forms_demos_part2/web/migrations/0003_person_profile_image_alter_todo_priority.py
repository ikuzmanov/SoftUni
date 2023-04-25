# Generated by Django 4.1.5 on 2023-02-02 20:12

from django.db import migrations, models
import forms_demos_part2.web.validators


class Migration(migrations.Migration):

    dependencies = [
        ("web", "0002_person_todo_assignee"),
    ]

    operations = [
        migrations.AddField(
            model_name="person",
            name="profile_image",
            field=models.ImageField(blank=True, null=True, upload_to=""),
        ),
        migrations.AlterField(
            model_name="todo",
            name="priority",
            field=models.IntegerField(
                validators=[
                    forms_demos_part2.web.validators.ValueInRangeValidator(1, 10)
                ]
            ),
        ),
    ]