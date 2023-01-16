from django.test import TestCase
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist
from task_manager.statuses.models import Status
from task_manager.users.models import User
from task_manager.utils import get_test_data


class StatusTest(TestCase):
    fixtures = ['statuses.json', 'users.json']

    @classmethod
    def setUpTestData(cls):
        cls.test_data = get_test_data()
        cls.user = User.objects.get(pk=2)
        cls.status = Status.objects.get(pk=1)

    def assertStatus(self, status, status_data):
        self.assertEqual(status.__str__(), status_data['name'])

    def test_index_page(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('statuses:status_index'))
        self.assertEqual(response.status_code, 200)

        statuses = Status.objects.all()
        self.assertQuerysetEqual(
            response.context['statuses'],
            statuses,
            ordered=False
        )

    def test_create_page(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('statuses:status_create'))
        self.assertEqual(response.status_code, 200)

    def test_create(self):
        self.client.force_login(self.user)
        new_status_data = self.test_data['statuses']['new']
        response = self.client.post(
            reverse('statuses:status_create'),
            new_status_data
        )

        self.assertRedirects(response, reverse('statuses:status_index'))
        created_status = Status.objects.get(name=new_status_data['name'])
        self.assertStatus(created_status, new_status_data)

    def test_update_page(self):
        self.client.force_login(self.user)
        exist_status_data = self.test_data['statuses']['existing']
        exist_status = Status.objects.get(name=exist_status_data['name'])
        response = self.client.get(reverse(
            'statuses:status_update',
            args=[exist_status.pk]
        ))
        self.assertEqual(response.status_code, 200)

    def test_update(self):
        self.client.force_login(self.user)
        exist_status_data = self.test_data['statuses']['existing']
        new_status_data = self.test_data['statuses']['new']
        exist_status = Status.objects.get(name=exist_status_data['name'])
        response = self.client.post(
            reverse('statuses:status_update', args=[exist_status.pk]),
            new_status_data,
        )

        self.assertRedirects(response, reverse('statuses:status_index'))
        updated_status = Status.objects.get(name=new_status_data['name'])
        self.assertStatus(updated_status, new_status_data)

    def test_delete_page(self):
        self.client.force_login(self.user)
        exist_status_data = self.test_data['statuses']['existing']
        exist_status = Status.objects.get(name=exist_status_data['name'])
        response = self.client.get(reverse(
            'statuses:status_delete',
            args=[exist_status.pk])
        )
        self.assertEqual(response.status_code, 200)

    def test_delete(self):
        self.client.force_login(self.user)
        exist_status_data = self.test_data['statuses']['existing']
        exist_status = Status.objects.get(name=exist_status_data['name'])
        response = self.client.post(reverse(
            'statuses:status_delete',
            args=[exist_status.pk]
        ))

        self.assertRedirects(response, reverse('statuses:status_index'))
        with self.assertRaises(ObjectDoesNotExist):
            Status.objects.get(name=exist_status_data['name'])
