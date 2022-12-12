from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404


# Create your views here.
def sample_view(request, department_id):
    result = f"path:{request.path}<br> POST: {request.POST}<br> path ifno: {request.path_info} <br> GET: {request.GET}" \
             f" <br> port: {request.get_port}<br> get_host: {request.get_host}<br> id as arg: {department_id}"
    return HttpResponse(result)
