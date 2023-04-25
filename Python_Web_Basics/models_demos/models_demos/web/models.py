from datetime import date

from django.db import models

from models_demos.web.validators import validate_before_today


# Create your models here.

class AuditInfoMixin(models.Model):
    class Meta:
        # no table will be created in DB
        # can be inherited in other models
        abstract = True

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)


class Department(AuditInfoMixin, models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return f"[ID: {self.id}] Name: {self.name}"

    def get_absolute_url(self):
        pass


class Project(AuditInfoMixin, models.Model):
    name = models.CharField(max_length=30)
    code_name = models.CharField(max_length=10, unique=True)
    deadline = models.DateField()


class Employee(AuditInfoMixin, models.Model):
    class Meta:
        ordering = ('years_of_experience', '-age')

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=40)
    review = models.TextField()
    years_of_experience = models.PositiveIntegerField()
    start_date = models.DateField(validators=(validate_before_today, ))
    email = models.EmailField(unique=True)
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

    @property
    def year_of_employment(self):
        return date.today() - self.start_date

    def __str__(self):
        return f'ID: {self.pk}; Name: {self.full_name}'


class AccessCard(models.Model):
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE,
                                    primary_key=True)


class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'

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
