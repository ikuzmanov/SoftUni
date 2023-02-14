from django import forms

from expense_tracker.expense.models import Expense


class ExpenseCreateForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = "__all__"
