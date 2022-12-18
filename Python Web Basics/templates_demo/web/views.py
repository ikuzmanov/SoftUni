import random

from django.shortcuts import render


# Create your views here.
def index(request):
    context = {
        'title': 'My homepage',
        'body': 'This is the homepage of this project. Below you can find your random number for the day:',
        'randnum': random.random()
    }

    return render(request, "web/index.html", context)
