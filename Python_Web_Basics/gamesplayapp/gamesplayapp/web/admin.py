from django.contrib import admin

from gamesplayapp.web.models import Game, Profile


# Register your models here.
@admin.register(Profile)
# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(Game)
class CarAdmin(admin.ModelAdmin):
    pass
