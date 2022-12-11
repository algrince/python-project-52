from django.shortcuts import render
from django.views import View
from task_manager.users.models import User


class UserIndexView(View):

    def get(self, request, *args, **kwargs):
        users = User.object.all()
        return render(request, 'users/index.html', context={
            'users': users,
        })