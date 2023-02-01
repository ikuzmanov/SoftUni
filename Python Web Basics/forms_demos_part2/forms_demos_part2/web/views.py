from django.http import HttpResponse
from django.shortcuts import render

from forms_demos_part2.web.forms import TodoCreateForm, TodoForm


def index(request):
    form_class = TodoForm
    if request.method == "GET":
        form = form_class()
    else:
        form = form_class(request.POST)

        if form.is_valid():
            #form.save()
            return HttpResponse('All is valid')
        # return HttpResponse('Not valid')

    context = {
        'form': form
    }
    return render(request, 'index.html', context)
