from django.shortcuts import get_object_or_404

from gamesplayapp.web.models import Profile, Game


def get_user_profile():
    return Profile.objects.all().first()


def get_all_games():
    return Game.objects.all()


def get_game_by_id(id):
    return get_object_or_404(Game, pk=id)
