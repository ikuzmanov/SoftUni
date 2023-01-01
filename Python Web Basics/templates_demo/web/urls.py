from django.urls import path

from web.views import index, search, about

urlpatterns = [
    path("", index, name="index"),
    path("search", search, name="google search"),
    path("about", about, name="about")
]
