from django import forms
from .models import login

class TaskForm(forms.login):
    class Meta:
        model = login
        fields = ['title', 'description', 'completed']