from django.db import models


# Create your models here.
class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=40)
    review = models.TextField()
    years_of_experience = models.PositiveIntegerField
    start_date = models.DateField()
    email = models.EmailField(unique=True, editable=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    age = models.IntegerField(default=-1)
    works_full_time = models.BooleanField(null=False)
    level = models.CharField(max_length=25,  choices=(
        ('jr', 'Junior'),
        ('reg', 'Regular'),
        ('sr', 'Senior')
    ))

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return f'ID: {self.pk}; Name: {self.full_name}'


class NullBlankDemo(models.Model):
    x = models.IntegerField(
        blank=True,
        null=False,
    )

    null = models.IntegerField(
        blank=False,
        null=True,
    )

    blank_null = models.IntegerField(
        blank=True,
        null=True,
    )

    default = models.IntegerField(
        blank=False,
        null=False,
    )
