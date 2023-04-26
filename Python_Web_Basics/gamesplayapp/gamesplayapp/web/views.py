from django.http import HttpResponse
from django.shortcuts import render, redirect
from gamesplayapp.web.core.tools import get_user_profile
from gamesplayapp.web.forms import ProfileForm


def index(request):
    profile = get_user_profile()
    context = {
        "profile": profile,
    }
    return render(request, 'home-page.html', context)


def create_profile(request):
    profile = get_user_profile()
    form = ProfileForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('index')

    context = {
        "profile": profile,
        "form": form,
    }
    return render(request, 'profile/create-profile.html', context)


def dashboard(request):
    profile = get_user_profile()
    context = {
        "profile": profile,
    }
    return render(request, 'dashboard.html', context)


def create_game(request):
    profile = get_user_profile()
    context = {
        "profile": profile,
    }
    return render(request, 'game/create-game.html', context)


def details_game(request):
    profile = get_user_profile()
    context = {
        "profile": profile,
    }
    return render(request, 'game/details-game.html', context)


def edit_game(request):
    profile = get_user_profile()
    context = {
        "profile": profile,
    }
    return render(request, 'game/edit-game.html', context)


def delete_game(request):
    profile = get_user_profile()
    context = {
        "profile": profile,
    }
    return render(request, 'game/delete-game.html', context)


def details_profile(request):
    profile = get_user_profile()
    context = {
        "profile": profile,
    }
    return render(request, 'profile/details-profile.html', context)


def edit_profile(request):
    profile = get_user_profile()
    context = {
        "profile": profile,
    }
    return render(request, 'profile/edit-profile.html', context)


def delete_profile(request):
    profile = get_user_profile()
    context = {
        "profile": profile,
    }
    return render(request, 'profile/delete-profile.html', context)
