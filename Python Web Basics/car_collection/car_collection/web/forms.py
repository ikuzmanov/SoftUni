from django import forms

from car_collection.web.models import Profile, Car


class CreateUserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ("username", "email", "age", "password")
        widgets = {
            'password': forms.PasswordInput(),
        }


class CreateCarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ("type", "model", "year", "image_url", "price")
