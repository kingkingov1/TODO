from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'is_done', 'is_delete']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'description': forms.Textarea(
                attrs={'class': 'form-control', 'rows': 10, 'placeholder': 'Description', 'style': 'height: 119px;'}),
            'is_done': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'is_delete': forms.CheckboxInput(attrs={'class': 'form-check-input'}),

        }


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("email",)
