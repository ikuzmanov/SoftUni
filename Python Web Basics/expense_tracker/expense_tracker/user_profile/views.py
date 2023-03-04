from django.shortcuts import render, redirect

from expense_tracker.expense.models import Expense
from expense_tracker.user_profile.forms import UserProfileEditForm, UserProfileDeleteForm
from expense_tracker.user_profile.models import UserProfile


# Create your views here.

def profile_page(request):
    user_profile = UserProfile.objects.all().first()
    expenses = Expense.objects.all()
    budget_left = user_profile.budget - sum(exp.price for exp in expenses)
    expenses_count = len(expenses)

    context = {
        "user_profile": user_profile,
        "expenses_count": expenses_count,
        "budget_left": budget_left,
    }
    return render(request, "profile/profile.html", context)


def edit_profile(request):
    user_profile = UserProfile.objects.all().first()
    if request.method == "GET":
        form = UserProfileEditForm(instance=user_profile)
    else:
        form = UserProfileEditForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('profile page')
    context = {
        "form": form,
    }
    return render(request, "profile/profile-edit.html", context)


def delete_profile(request):
    user_to_delete = UserProfile.objects.all().first()
    if request.method == "POST":
        user_to_delete.delete()
        return redirect('index')

    return render(request, 'profile/profile-delete.html')
