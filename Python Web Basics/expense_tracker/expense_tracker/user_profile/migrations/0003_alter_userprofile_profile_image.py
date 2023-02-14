# Generated by Django 4.1.6 on 2023-02-13 20:47

from django.db import migrations, models
import expense_tracker.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ("user_profile", "0002_alter_userprofile_first_name_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userprofile",
            name="profile_image",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to="profile_images/",
                validators=[
                    expense_tracker.core.validators.validate_file_less_than_5MB
                ],
            ),
        ),
    ]