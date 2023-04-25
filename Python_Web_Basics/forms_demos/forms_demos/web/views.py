from django.shortcuts import render

from forms_demos.web.forms import PersonForm, PersonCreateForm
from forms_demos.web.models import Person


# Create your views here.
def index_form(request):
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


def index_model_form(request):
    if request.method == 'GET':
        form = PersonCreateForm()
    else:

        form = PersonCreateForm(request.POST)
        if form.is_valid():
            form.save()
            # pets = form.cleaned_data.pop('pets')
            # person = Person.objects.create(**form.cleaned_data)
            # person.pets.set(pets)
            # person.save()
            # print(form.cleaned_data)

    context = {
        'form': form
    }
    return render(request, 'model-forms.html', context)
