from django.contrib import admin

from car_collection.web.models import Profile, Car


# Register your models here.
@admin.register(Profile)
# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    pass