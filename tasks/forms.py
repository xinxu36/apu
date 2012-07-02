from django import forms

class newTask(forms.Form):
    task = forms.CharField(max_length = 300)
    due_date = forms.DateTimeField()