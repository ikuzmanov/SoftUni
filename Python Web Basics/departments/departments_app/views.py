from random import choice

from django.http import HttpResponse, Http404, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404, redirect


# Create your views here.
def sample_view(request, department_id):
    result = f"path:{request.path}<br> POST: {request.POST}<br> path ifno: {request.path_info} <br> GET: {request.GET}" \
             f" <br> port: {request.get_port}<br> get_host: {request.get_host}<br> id as arg: {department_id}"
    return HttpResponse(result)


def redirect_to_foreign_url(request):
    urls_to_redirect = ("https://softuni.bg", "https://google.com", "https://abv.bg")
    choice_to_redirect = choice(urls_to_redirect)
    return redirect(choice_to_redirect)


def page_not_found(request):
    raise Http404()
