from django import forms
from django.utils.translation import ugettext_lazy as _

class CreateAccountForm(forms.Form):
    name = forms.CharField(label=_('Name'), widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'First name and last name'
    }))
    company_name = forms.CharField(label=_('Company Name'), widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Name of your company'
    }))
    email = forms.EmailField(label=_('Email'), widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Official email address'
    }))
    password = forms.CharField(label=_('Password'), widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Password'
    }))
    confirm_password = forms.CharField(label=_('Confirm Password'), widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Type password again'
    }))