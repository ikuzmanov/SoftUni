# Generated by Django 4.1.5 on 2023-01-11 17:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("web", "0013_category"),
    ]

    operations = [
        migrations.AddField(
            model_name="employee",
            name="years_of_experience",
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="category",
            name="parent_category",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.RESTRICT,
                to="web.category",
            ),
        ),
    ]