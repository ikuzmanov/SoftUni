from django.http import HttpResponse
from django.urls import path

from departments_app.views import sample_view, redirect_to_foreign_url, page_not_found

urlpatterns = [
    path('<int:department_id>', sample_view),
    path('redirect_foreign', redirect_to_foreign_url, name="redirect to foreign url"),
    path("not-found", page_not_found)
]
