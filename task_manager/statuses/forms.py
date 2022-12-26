from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Status


class StatusForm(forms.ModelForm):

    name = forms.CharField(
        label=_('Status name'),
        min_length=6,
        max_length=30,
        widget=forms.TextInput(attrs={
            'class': 'form-control mb-3',
            'placeholder': _('Status name'),
        })
    )

    class Meta:
        model = Status
        fields = ['name']