from django import forms

class ContactForm(forms.Form):
    subject = forms.CharField()
    sender = forms.EmailField()
    message = forms.CharField()
    cc_myself = forms.BooleanField(required=False)