from django import forms
from .models import ToDo


class CreateTaskForm(forms.ModelForm):

    class Meta:
        model = ToDo
        fields = "__all__"


class UpdateTaskForm(forms.ModelForm):

    class Meta:
        model = ToDo
        fields = [
            'completed'
        ]
