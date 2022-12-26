from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.utils.translation import gettext_lazy as _
from .models import User


class UserForm(UserCreationForm):

    first_name = forms.CharField(
        label=_('First name'),
        widget=forms.TextInput(attrs={
            'class': 'form-control mb-3',
            'placeholder': _('First name'),
        })
    )

    last_name = forms.CharField(
        label=_('Last name'),
        widget=forms.TextInput(attrs={
            'class': 'form-control mb-3',
            'placeholder': _('Last name'),
        })
    )

    username = forms.CharField(
        label=_('Username'),
        widget=forms.TextInput(attrs={
            'class': 'form-control mb-3',
            'placeholder': _('Username'),
        })
    )

    password1 = forms.CharField(
        label=_('Password'),
        min_length=6,
        max_length=25,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': _('Password'),
        }),
    )

    password2 = forms.CharField(
        label=_('Password confirmation'),
        min_length=6,
        max_length=25,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': _('Password confirmation'),
        }),
    )

    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "username",
            "password1",
            "password2",
        ]
        max_lenghts = {
            'first_name': 30,
            'username': 20,
        }
        labels = {
            'first_name': _('First name'),
            'last_name': _('Last name'),
            'username': _('Username')
        }
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control mb-3',
                'placeholder': _('First name'),
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control mb-3',
                'placeholder': _('Last name'),
            }),
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': _('Username'),
            }),
        }


class ChangeUserForm(UserForm, UserChangeForm):

    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "username",
            "password1",
            "password2",
        ]
