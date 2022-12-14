from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views import View
from django.views.generic.base import ContextMixin
from django.urls import reverse_lazy
from task_manager.users.models import User
from task_manager.users.forms import UserForm

class UserIndexView(ListView):

    model = User
    template_name = "users/index.html"
    context_object_name = "users"
    

class UserFormCreateView(CreateView):

    model = User
    fields = "__all__"
    template_name = "users/create_user.html"


class UserFormUpdateView(UpdateView):

    model = User
    fields = "__all__"
    template_name = "users/update_user.html"


class UserDeleteView(DeleteView):

    model = User
    template_name = "users/delete_user.html"
    success_url = reverse_lazy('index')