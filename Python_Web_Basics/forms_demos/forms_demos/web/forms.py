from django import forms

from forms_demos.web.models import Person


class PersonForm(forms.Form):
    OCCUPANCIES = (
        (1, 'Child'),
        (2, 'High schoolStudent'),
        (3, 'Student'),
        (4, 'Adult')
    )
    your_name = forms.CharField(max_length=30, help_text="Enter your name", widget=forms.TextInput(
        attrs={
            'class': 'form-control-lg',
            'placeholder': 'Enter your name',
        }
    ))
    age = forms.IntegerField(required=False, label='Your age', initial=0)
    email = forms.EmailField()
    occupancy = forms.ChoiceField(choices=OCCUPANCIES, widget=forms.RadioSelect())
    story = forms.CharField(widget=forms.Textarea())


class PersonCreateForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'
        # exclude = ('pets', )
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'})
        }
        help_texts = {
            'name': 'Your name'
        }
        labels = {
            'age' : 'the age',
        }
