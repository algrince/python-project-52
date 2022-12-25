from django.test import TestCase
from django.urls import reverse


class UsersTest(TestCase):

    def test_index_page(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_create_page(self):
        response = self.client.get(reverse('user_create'))
        self.assertEqual(response.status_code, 200)

    def test_update_page(self):
        response = self.client.get(reverse('user_update'))
        self.assertEqual(response.status_code, 200)

    def test_delete_page(self):
        response = self.client.get(reverse('user_delete'))
        self.assertEqual(response.status_code, 200)
