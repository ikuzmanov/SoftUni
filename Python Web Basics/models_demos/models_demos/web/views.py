from django.shortcuts import render

from models_demos.web.models import Employee, Department


# Create your views here.
def index(request):
    employees = Employee.objects.filter(department__name="Engineering")
    department = Department.objects.get(pk=1)
    context = {
        'employees': employees,
        'department': department
    }
    return render(request, 'index.html', context)
