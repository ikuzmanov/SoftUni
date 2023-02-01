from django import forms
from django.core.exceptions import ValidationError

from forms_demos_part2.web.models import Todo
from forms_demos_part2.web.validators import validate_text, ValueInRangeValidator


class TodoForm(forms.Form):
    text = forms.CharField(max_length=30, validators=(validate_text,), error_messages={'required': "FILL IT OUT!"})
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

    def clean(self):
        return super().clean()

    def clean_text(self):
        """
        Used for :
        1. Transform data into desired format/format
        2. Validation
        """
        return self.cleaned_data['text'].lower()

    def clean_assignee(self):
        assignee = self.cleaned_data['assignee']
        if assignee.todo_set.count() >= Todo.MAX_TODOS_COUNT_PER_PERSON:
            raise ValidationError(f'{assignee} already has max todos assigned')
        return assignee
