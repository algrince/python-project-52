from django.forms import ModelForm
from task_manager.users.models import User


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = []