from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    REQUIRED_FIELDS = [
        'first_name',
        'last_name',
    ]
    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.get_full_name()
