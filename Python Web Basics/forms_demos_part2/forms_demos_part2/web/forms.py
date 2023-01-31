from django import forms

from forms_demos_part2.web.models import Todo
from forms_demos_part2.web.validators import validate_text, ValueInRangeValidator


class TodoForm(forms.Form):
    text = forms.CharField(validators=(validate_text,))
    is_done = forms.BooleanField(required=False, )
    priority = forms.IntegerField(validators=(ValueInRangeValidator(1, 10),))

    # def clean_text(self):
    #     pass
    #
    # def clean_priority(self):
    #     pass
    #


class TodoCreateForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = '__all__'
