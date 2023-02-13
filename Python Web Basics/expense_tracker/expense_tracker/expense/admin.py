from django.contrib import admin

from expense_tracker.expense.models import Expense


@admin.register(Expense)
# Register your models here.
class ExpenseAdmin(admin.ModelAdmin):
    pass
