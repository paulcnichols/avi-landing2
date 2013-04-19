# forms.py
from django import forms

class InterestedForm(forms.Form):
    email = forms.EmailField()
