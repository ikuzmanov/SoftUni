from django import forms

from expense_tracker.user_profile.models import UserProfile


class UserProfileBaseForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ("budget", "first_name", "last_name", "profile_image")


class UserProfileCreateForm(UserProfileBaseForm):
    pass


class UserProfileEditForm(UserProfileBaseForm):
    pass


class UserProfileDeleteForm(UserProfileBaseForm):
    pass
