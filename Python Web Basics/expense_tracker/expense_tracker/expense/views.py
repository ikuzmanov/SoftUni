from django.shortcuts import render

from expense_tracker.user_profile.models import UserProfile


# Create your views here.

def index(request):
    context = {
        "user_profile": UserProfile.objects.all().first()
    }
    return render(request, 'base.html', context)


def create_expense(request):
    context = {
        "user_profile": UserProfile.objects.all().first()
    }
    return render(request, 'expense/expense-create.html', context)


def edit_expense(request, pk):
    context = {
        "user_profile": UserProfile.objects.all().first()
    }
    return render(request, 'expense/expense-edit.html', context)


def delete_expense(request, pk):
    context = {
        "user_profile": UserProfile.objects.all().first()}
    return render(request, 'expense/expense-delete.html', context)
