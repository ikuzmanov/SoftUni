from django import forms
from django.shortcuts import render

from forms_demos.web.models import Person


class PersonForm(forms.Form):
    OCCUPANCIES = (
        (1, 'Child'),
        (2, 'High schoolStudent'),
        (3, 'Student'),
        (4, 'Adult')
    )
    your_name = forms.CharField(max_length=30, help_text="Enter your name", widget = forms.TextInput(
        attrs={
            'class': 'form-control-lg',
            'placeholder': 'Enter your name',
        }
    ))
    age = forms.IntegerField(required=False, label='Your age', initial=0)
    email = forms.EmailField()
    occupancy = forms.ChoiceField(choices=OCCUPANCIES, widget=forms.RadioSelect())
    story = forms.CharField(widget=forms.Textarea())


# Create your views here.
def index(request):
    name = None
    if request.method == 'GET':
        form = PersonForm()
    else:  # request.method == 'POST'
        form = PersonForm(request.POST)
        if form.is_valid():  # 1. validates the form 2.fills 'cleaned_data'
            name = form.cleaned_data['your_name']
            Person.objects.create(name=name)
    context = {
        'form': form,
        'name': name,
    }

    return render(request, 'index.html', context)
