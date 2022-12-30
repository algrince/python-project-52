from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import UserPassesTestMixin
from django.utils.translation import gettext_lazy as _
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib import messages
from .models import User
from .forms import UserForm, ChangeUserForm


class UserIndexView(
        ListView
):

    model = User
    template_name = 'users/index.html'
    context_object_name = 'users'


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
        UserPassesTestMixin,
        SuccessMessageMixin,
        UpdateView,
):

    model = User
    form_class = ChangeUserForm
    template_name = 'users/update_user.html'

    success_url = reverse_lazy('users:index')
    success_message = "%(username)s was updated successfully"

    def test_func(self):
        return self.get_object() == self.request.user

    def handle_no_permission(self):
        if not self.request.user.is_authenticated:
            messages.error(
                self.request,
                _('You need to be logged in for changing the user!')
            )
            return redirect('login')
        messages.error(
            self.request,
            _("You can't change another user!")
        )
        return redirect('users:index')


class UserDeleteView(
        UserPassesTestMixin,
        SuccessMessageMixin,
        DeleteView,
):

    model = User
    template_name = "users/delete_user.html"

    success_url = reverse_lazy('users:index')
    success_message = "%(username)s was deleted successfully"

    def test_func(self):
        return self.get_object() == self.request.user

    def handle_no_permission(self):
        if not self.request.user.is_authenticated:
            messages.error(
                self.request,
                _('You need to be logged in for deleting the user!')
            )
            return redirect('login')
        messages.error(
            self.request,
            _("You can't delete another user!")
        )
        return redirect('users:index')
