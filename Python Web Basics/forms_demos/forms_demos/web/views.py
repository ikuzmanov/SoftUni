from django import forms
from django.shortcuts import render

from forms_demos.web.models import Person


class NameForm(forms.Form):
    your_name = forms.CharField(max_length=30)


# Create your views here.
def index(request):
    name = None
    if request.method == 'GET':
        form = NameForm()
    else:  # request.method == 'POST'
        form = NameForm(request.POST)
        form.is_valid()
        name = form.cleaned_data['your_name']
        Person.objects.create(name=name)
    context = {
        'form': form,
        'name': name,
    }

    return render(request, 'index.html', context)
