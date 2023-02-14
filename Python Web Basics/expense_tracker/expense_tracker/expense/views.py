from django.shortcuts import render

from expense_tracker.expense.forms import ExpenseCreateForm
from expense_tracker.expense.models import Expense
from expense_tracker.user_profile.forms import UserProfileCreateForm
from expense_tracker.user_profile.models import UserProfile


# Create your views here.

def index(request):
    if request.method == 'POST':
        form = UserProfileCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

    else:
        form = UserProfileCreateForm()
    context = {
        "user_profile": UserProfile.objects.all().first(),
        "form": form,
        "expenses": Expense.objects.all(),
    }
    return render(request, 'index.html', context)


def create_expense(request):
    form = ExpenseCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        "form": form,
    }
    return render(request, 'expense/expense-create.html', context)


def edit_expense(request, pk):
    context = {
    }
    return render(request, 'expense/expense-edit.html', context)


def delete_expense(request, pk):
    context = {}
    return render(request, 'expense/expense-delete.html', context)
