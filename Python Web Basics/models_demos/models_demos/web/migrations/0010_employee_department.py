# Generated by Django 4.1.5 on 2023-01-10 21:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("web", "0009_department"),
    ]

    operations = [
        migrations.AddField(
            model_name="employee",
            name="department",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="web.department",
            ),
            preserve_default=False,
        ),
    ]
