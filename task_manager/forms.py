from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.utils.translation import gettext_lazy as _



class UserAuthenticationForm(AuthenticationForm):
    
    username = forms.CharField(
        label=_('Username'),
        widget=forms.TextInput(attrs={
            'class': 'w-50 form-control mb-3',
            'placeholder': _('Username'),
        })
    )

    password = forms.CharField(
        label=_('Password'),
        widget=forms.PasswordInput(attrs={
            'class': 'w-50 form-control mb-3',
            'placeholder': _('Password'),
        })
    )