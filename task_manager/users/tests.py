from django.test import TestCase
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist
from task_manager.users.models import User
from task_manager.utils import get_test_data


class UsersTest(TestCase):
    fixtures = ['users.json']

    @classmethod
    def setUpTestData(cls):
        cls.test_data = get_test_data()
        cls.user = User.objects.get(pk=2)

    def assertUser(self, user, user_data):
        self.assertEqual(user.__str__(), user.get_full_name())
        self.assertEqual(user.username, user_data['username'])

    def test_index_page(self):
        response = self.client.get(reverse('users:index'))
        self.assertEqual(response.status_code, 200)

        users = User.objects.all()
        self.assertQuerysetEqual(
            response.context['users'],
            users,
            ordered=False,
        )

    def test_create_page(self):
        response = self.client.get(reverse('users:user_create'))
        self.assertEqual(response.status_code, 200)

    def test_create(self):
        new_user_data = self.test_data['users']['new']
        response = self.client.post(reverse('users:user_create'), new_user_data)

        self.assertRedirects(response, reverse('login'))
        created_user = User.objects.get(username=new_user_data['username'])
        self.assertUser(created_user, new_user_data)

    def test_update_page(self):
        exist_user_data = self.test_data['users']['existing']
        exist_user = User.objects.get(username=exist_user_data['username'])
        self.client.force_login(self.user)
        response = self.client.get(reverse(
            'users:user_update',
            args=[exist_user.pk]
        ))
        self.assertEqual(response.status_code, 200)

    def test_update(self):
        exist_user_data = self.test_data['users']['existing']
        new_user_data = self.test_data['users']['new']
        exist_user = User.objects.get(username=exist_user_data['username'])
        self.client.force_login(self.user)
        response = self.client.post(
            reverse('users:user_update', args=[exist_user.pk]),
            new_user_data,
        )

        self.assertRedirects(response, reverse('users:index'))
        updated_user = User.objects.get(username=new_user_data['username'])
        self.assertUser(updated_user, new_user_data)

    def test_delete_page(self):
        exist_user_data = self.test_data['users']['existing']
        exist_user = User.objects.get(username=exist_user_data['username'])
        self.client.force_login(self.user)
        response = self.client.get(reverse(
            'users:user_delete',
            args=[exist_user.pk]
        ))
        self.assertEqual(response.status_code, 200)

    def test_delete(self):
        exist_user_data = self.test_data['users']['existing']
        exist_user = User.objects.get(username=exist_user_data['username'])
        self.client.force_login(self.user)
        reponse = self.client.post(reverse(
            'users:user_delete',
            args=[exist_user.pk]
        ))

        self.assertRedirects(reponse, reverse('users:index'))
        with self.assertRaises(ObjectDoesNotExist):
            User.objects.get(username=exist_user_data['username'])
