from django.urls import path

from web.views import index, search

urlpatterns = [
    path("", index, name="index"),
    path("search", search, name="google search")
]
