from django import forms
from django.forms.widgets import DateTimeInput

class newTask(forms.Form):
    task = forms.CharField(max_length = 300)
    due_date = forms.DateTimeField()