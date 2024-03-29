from django.urls import path

from expense_tracker.user_profile.views import profile_page, edit_profile, delete_profile


urlpatterns = [
    path("", profile_page, name="profile page"),
    path("edit/", edit_profile, name="edit profile"),
    path("delete/", delete_profile, name="delete profile"),
    ]