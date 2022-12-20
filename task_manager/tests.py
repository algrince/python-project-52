from django.test import TestCase
from django.urls import reverse


class AppTest(TestCase):

    def test_base_page(self):
        response = self.client.get(reverse('base'))
        self.assertEqual(response.status_code, 200)

    def test_login_page(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
