from django import forms
from django.core import validators


class Account(forms.Form):
    name = forms.CharField(label="Enter your full name")
    father_name = forms.CharField(label="Enter your Father name")
    email = forms.CharField(widget= forms.EmailInput, validators = [validators.EmailValidator(message="Enter a valid email")])
    age = forms.CharField(widget=forms.NumberInput)
    birthday = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
