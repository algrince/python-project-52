from django import forms
from task_manager.users.models import User


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = "__all__"