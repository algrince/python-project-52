from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, AccessMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext_lazy as _
from django.urls import reverse_lazy
from task_manager.users.models import User
from task_manager.users.forms import UserForm, ChangeUserForm


class UserIndexView(
        ListView
):

    model = User
    template_name = 'users/index.html'
    context_object_name = "users"
    

class UserFormCreateView(
        SuccessMessageMixin,
        CreateView
    ):

    model = User
    form_class = UserForm
    template_name = 'users/create_user.html'

    success_url = reverse_lazy('login')
    success_message = "%(username)s was created successfully"


class UserFormUpdateView(
        PermissionRequiredMixin,
        LoginRequiredMixin,
        UpdateView
):

    model = User
    form_class = ChangeUserForm
    permission_required = 'users.change_user'
    template_name = ('users/update_user.html')

    success_url = reverse_lazy('index')
    success_message = "%(username)s was updated successfully"

    login_url = 'login'
    permission_denied_message = _("You can't update other user's account!")


class UserDeleteView(
    PermissionRequiredMixin,
    LoginRequiredMixin,
    DeleteView,
):

    model = User
    permission_required = ('users.delete_user')
    template_name = "users/delete_user.html"

    success_url = reverse_lazy('index')
    success_message = "%(username)s was deleted successfully"

    login_url = 'login'
    permission_denied_message = _("You can't delete other user's account!")