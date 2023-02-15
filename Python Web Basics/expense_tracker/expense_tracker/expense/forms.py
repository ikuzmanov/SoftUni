from django import forms

from expense_tracker.expense.models import Expense


class ExpenseBaseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ("title", "description", "expense_image", "price")
        labels = {'expense_image': 'Link to Image'}


class ExpenseCreateForm(ExpenseBaseForm):
    pass


class ExpenseEditForm(ExpenseBaseForm):
    pass


class ExpenseDeleteForm(ExpenseBaseForm):
    def __init__(self, *args, **kwargs):
        super(ExpenseDeleteForm, self).__init__(*args, **kwargs)
        for key in self.fields.keys():
            self.fields[key].widget.attrs['readonly'] = True
