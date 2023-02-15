from django.urls import path

from expense_tracker.expense.views import index, create_expense, edit_expense, delete_expense

urlpatterns = [
    path("", index, name="index"),
    path("create/", create_expense, name="create expense"),
    path("edit/<int:id>", edit_expense, name="edit expense"),
    path("delete/<int:id>", delete_expense, name="delete expense"),
    ]