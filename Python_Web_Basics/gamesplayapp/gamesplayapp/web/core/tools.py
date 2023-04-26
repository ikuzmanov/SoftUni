from gamesplayapp.web.models import Profile


def get_user_profile():
    return Profile.objects.all().first()
