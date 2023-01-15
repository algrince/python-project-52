from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext_lazy as _
from django.urls import reverse_lazy
from .models import Status
from .forms import StatusForm


class StatusIndexView(
        LoginRequiredMixin,
        ListView,
):

    model = Status
    template_name = 'statuses/index.html'
    context_object_name = 'statuses'

    login_url = 'login'
    permission_denied_message = _('You should be logged in to view statuses!')
    redirect_field_name = reverse_lazy('status_index')


class StatusFormCreateView(
    LoginRequiredMixin,
    SuccessMessageMixin,
    CreateView,
):

    model = Status
    form_class = StatusForm
    template_name = 'statuses/create_status.html'

    login_url = 'login'
    permission_denied_message = _('You should be logged in to create a status!')
    redirect_field_name = reverse_lazy('statuses:status_index')

    success_url = reverse_lazy('statuses:status_index')
    success_message = "Status was created successfully"


class StatusFormUpdateView(
    LoginRequiredMixin,
    SuccessMessageMixin,
    UpdateView,
):

    model = Status
    form_class = StatusForm
    template_name = 'statuses/update_status.html'

    login_url = 'login'
    permission_denied_message = _('You should be logged in to change a status!')
    redirect_field_name = reverse_lazy('statuses:status_index')

    success_url = reverse_lazy('statuses:status_index')
    success_message = "Status was updated successfully"


class StatusDeleteView(
    LoginRequiredMixin,
    SuccessMessageMixin,
    DeleteView,
):

    model = Status
    template_name = 'statuses/delete_status.html'

    login_url = 'login'
    permission_denied_message = _('You should be logged in to delete a status!')
    redirect_field_name = reverse_lazy('statuses:status_index')

    success_url = reverse_lazy('statuses:status_index')
    success_message = "Status was deleted successfully"
