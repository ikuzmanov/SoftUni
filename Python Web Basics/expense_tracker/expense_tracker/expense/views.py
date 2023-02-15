from django.shortcuts import render, get_object_or_404, redirect

from expense_tracker.expense.forms import ExpenseCreateForm, ExpenseEditForm, ExpenseDeleteForm
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
    user_profile = UserProfile.objects.all().first()
    total_expenses = 0
    expenses = Expense.objects.all()
    for obj in expenses:
        total_expenses += obj.price

    context = {
        "user_profile": user_profile,
        "form": form,
        "expenses": expenses,
        "budget_left": user_profile.budget - total_expenses
    }
    return render(request, 'index.html', context)


def create_expense(request):
    form = ExpenseCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('index')
    context = {
        "form": form,
    }
    return render(request, 'expense/expense-create.html', context)


def edit_expense(request, id):
    expense = get_object_or_404(Expense, id=id)

    if request.method == "GET":
        form = ExpenseEditForm(instance=expense)
    else:
        form = ExpenseEditForm(request.POST, request.FILES, instance=expense)
        if form.is_valid():
            form.save()
            return redirect("index")
    context = {
        "form": form,
        "expense": expense
    }
    return render(request, 'expense/expense-edit.html', context)


def delete_expense(request, id):
    expense_to_delete = get_object_or_404(Expense, id=id)
    form = ExpenseDeleteForm(request.POST or None, instance=expense_to_delete)
    if form.is_valid():
        expense_to_delete.delete()
        return redirect('index')
    context = {
        "form": form,
    }
    return render(request, 'expense/expense-delete.html', context)
