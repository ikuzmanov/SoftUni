from django.http import HttpResponse
from django.shortcuts import render

from django001.tasks.models import Task


# Create your views here.
def bare_minimum_view(request):
    return HttpResponse("<h1>Hello world</h1>")


def show_all_tasks(request):
    all_tasks = Task.objects.order_by('priority').all()
    response = (f"{t.id}: {t.name} [PRIORITY: {t.priority}]<br>" for t in all_tasks)
    return HttpResponse(response)


def index(request):
    all_tasks = Task.objects.order_by('priority').all()
    context = {"tasks": all_tasks, "title": "Tasks", "header": "Tasks dashboard"}
    return render(request, 'index.html', context)
