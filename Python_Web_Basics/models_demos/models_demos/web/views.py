from django.shortcuts import render, get_object_or_404, redirect

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


def department_details(request, pk, slug):
    context = {
        'department': get_object_or_404(Department, pk=pk, slug=slug)
    }
    return render(request, 'department-details.html', context)


def delete_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    employee.delete()
    return redirect('index')
