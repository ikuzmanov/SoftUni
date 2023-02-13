from django.contrib import admin

from expense_tracker.user_profile.models import UserProfile


# Register your models here.
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    pass
