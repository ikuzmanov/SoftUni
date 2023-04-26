from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def index(request):
    return HttpResponse("Hello world!")


def create_profile(request):
    pass


def dashboard(request):
    pass


def create_game(request):
    pass


def details_game(request):
    pass


def edit_game(request):
    pass


def delete_game(request):
    pass


def details_profile(request):
    pass


def edit_profile(request):
    pass


def delete_profile(request):
    pass
