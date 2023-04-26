from django import forms
from gamesplayapp.web.models import Profile

class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['email', 'age', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }
