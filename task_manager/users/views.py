from django.shortcuts import render
from django.views import View
from task_manager.users.models import User
from task_manager.users.forms import UserForm

class UserIndexView(View):

    def get(self, request, *args, **kwargs):
        users = User.objects.all()
        return render(request, 'users/index.html', context={
            'users': users,
        })


class UserFormCreateView(View):

    def get(self, request, *args, **kwargs):
        form = UserForm()
        return render(request, 'users/create_user.html', {'form': form})

    
    def post(self, request, *args, **kwargs):
        form = UserForm(request.POST)
        pass
