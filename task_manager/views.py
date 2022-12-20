from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.utils.translation import gettext_lazy as _
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import UserAuthenticationForm



def index(request):
    return render(request, 'base.html')


class UserLoginView(LoginView):
    template_name = 'login.html'
    authentication_form = UserAuthenticationForm

    def get_success_url(self):
        messages.success(self.request, _('Tou are successfully logged in'))
        return reverse_lazy('base')


class UserLogoutView(LogoutView):

    def get_success_url(self):
        messages.success(self.request, _('You are successfully logged out'))
        return reverse_lazy('base')