from django.urls import path

from forms_demos_part2.web.views import index

urlpatterns = [
    path('', index, name='index')
]