from django.http import HttpResponse
from django.shortcuts import render

from forms_demos_part2.web.forms import TodoCreateForm


def index(request):
    if request.method == "GET":
        form = TodoCreateForm()
    else:
        form = TodoCreateForm(request.POST)

        if form.is_valid():
            return HttpResponse('All is valid')
        # return HttpResponse('Not valid')

    context = {
        'form': form
    }
    return render(request, 'index.html', context)
