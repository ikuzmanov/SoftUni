from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'home-page.html')


def create_profile(request):
    return render(request, 'profile/create-profile.html')


def dashboard(request):
    return render(request, 'dashboard.html')


def create_game(request):
    return render(request, 'game/create-game.html')


def details_game(request):
    return render(request, 'game/details-game.html')


def edit_game(request):
    return render(request, 'game/edit-game.html')


def delete_game(request):
    return render(request, 'game/delete-game.html')


def details_profile(request):
    return render(request, 'profile/details-profile.html')


def edit_profile(request):
    return render(request, 'profile/edit-profile.html')


def delete_profile(request):
    return render(request, 'profile/delete-profile.html')
