import random

from django.shortcuts import render, redirect


# Create your views here.

def return_hello():
    return "HELLO FROM FUNC"


def index(request):
    context = {
        'title': 'My homepage',
        'body': 'This is the homepage of this project. Below you can find your random number for the day:',
        'randnum': random.random(),
        'randomlist': ['cat', 'dog', 'elephant', 'tiger'],
        'hello_func': return_hello(),
        # 'students': ['Pesho', 'Gosho', 'Ivan', 'Maria'],
        'teachers': ['Dimitar', 'Radina', 'Petia'],
        'values': tuple(range(1, 50))
    }

    return render(request, "web/index.html", context)


def search(request):
    return redirect("https://google.com")
