from django.shortcuts import render, redirect, get_object_or_404
from gamesplayapp.web.core.tools import get_user_profile, get_all_games, get_game_by_id
from gamesplayapp.web.forms import ProfileCreationForm, GameCreationForm, GameEditForm, GameDeleteForm
from gamesplayapp.web.models import Game


def index(request):
    profile = get_user_profile()
    context = {
        "profile": profile,
    }
    return render(request, 'home-page.html', context)


def create_profile(request):
    profile = get_user_profile()
    form = ProfileCreationForm(request.POST or None)
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
    all_games = get_all_games()
    context = {
        "profile": profile,
        "all_games": all_games,
    }
    return render(request, 'dashboard.html', context)


def create_game(request):
    profile = get_user_profile()
    form = GameCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('dashboard')
    context = {
        "profile": profile,
        "form": form,
    }
    return render(request, 'game/create-game.html', context)


def details_game(request, id):
    profile = get_user_profile()
    game = get_game_by_id(id)
    context = {
        "profile": profile,
        "game": game,
    }
    return render(request, 'game/details-game.html', context)


def edit_game(request, id):
    profile = get_user_profile()
    game = get_game_by_id(id)
    form = GameEditForm(request.POST or None, instance=game)
    if form.is_valid():
        form.save()
        return redirect('dashboard')

    context = {
        "profile": profile,
        "game": game,
        "form": form,
    }
    return render(request, 'game/edit-game.html', context)


def delete_game(request, id):
    profile = get_user_profile()
    game = get_game_by_id(id)
    form = GameDeleteForm(request.POST or None, instance=game)
    if form.is_valid():
        game.delete()
        return redirect('dashboard')
    context = {
        "profile": profile,
        "game": game,
        "form": form,
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
