from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from task_manager.users.models import User
from task_manager.users.forms import UserForm, ChangeUserForm

class UserIndexView(ListView):

    model = User
    template_name = "users/index.html"
    context_object_name = "users"
    

class UserFormCreateView(CreateView):

    model = User
    form_class = UserForm
    template_name = "users/create_user.html"
    success_url = reverse_lazy('index')


class UserFormUpdateView(
        LoginRequiredMixin,
        PermissionRequiredMixin, 
        UpdateView
):

    model = User
    permission_required = ('users.change_user')
    form_class = ChangeUserForm
    template_name = "users/update_user.html"
    success_url = reverse_lazy('index')


class UserDeleteView(
    LoginRequiredMixin,
    PermissionRequiredMixin, 
    DeleteView,
):

    model = User
    permission_required = ('users.delete_user')
    template_name = "users/delete_user.html"
    success_url = reverse_lazy('index')