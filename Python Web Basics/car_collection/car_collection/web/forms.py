from django import forms

from car_collection.web.models import Profile, Car


class CarBaseForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ("type", "model", "year", "image_url", "price")


class CreateUserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ("username", "email", "age", "password")
        widgets = {
            'password': forms.PasswordInput(),
        }

class EditUserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"

class CreateCarForm(CarBaseForm):
    pass


class EditCarForm(CarBaseForm):
    pass


class DeleteCarForm(CarBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.required = False
