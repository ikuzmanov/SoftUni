from django.db import models


# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return f"[ID: {self.id}] Name: {self.name}"


class Project(models.Model):
    name = models.CharField(max_length=30)
    code_name = models.CharField(max_length=10, unique=True)
    deadline = models.DateField()


class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=40)
    review = models.TextField()
    years_of_experience = models.PositiveIntegerField()
    start_date = models.DateField()
    email = models.EmailField(unique=True, editable=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    age = models.IntegerField(default=-1)
    works_full_time = models.BooleanField(null=False)
    level = models.CharField(max_length=25, choices=(
        ('jr', 'Junior'),
        ('reg', 'Regular'),
        ('sr', 'Senior')
    ))

    # One-to-many
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    # Many-to-many
    projects = models.ManyToManyField(Project)

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return f'ID: {self.pk}; Name: {self.full_name}'


class AccessCard(models.Model):
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE,
                                    primary_key=True)


class Category(models.Model):
    name = models.CharField(max_length=35)
    parent_category = models.ForeignKey('Category', on_delete=models.RESTRICT, null=True, blank=True)

    def __str__(self):
        return f"Name:{self.name}"

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
