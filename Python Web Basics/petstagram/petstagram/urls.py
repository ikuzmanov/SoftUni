from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include('petstagram.accounts.urls')),
    path("photos/", include('petstagram.photos.urls')),
    path("pets/", include('petstagram.pets.urls')),
    path("", include('petstagram.common.urls')),
]
