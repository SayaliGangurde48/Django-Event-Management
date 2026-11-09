from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User


class AccountTests(TestCase):

    def test_home_page(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_user_registration(self):
        response = self.client.post(reverse('register'), {
            'first_name': 'Sayali',
            'last_name': 'Gangurde',
            'username': 'sayali',
            'email': 'sayali@example.com',
            'password1': 'TestPassword@123',
            'password2': 'TestPassword@123',
        })

        self.assertEqual(response.status_code, 302)
        self.assertTrue(User.objects.filter(username='sayali').exists())

    def test_user_login(self):
        User.objects.create_user(
            username='sayali',
            password='TestPassword@123'
        )

        response = self.client.post(reverse('login'), {
            'username': 'sayali',
            'password': 'TestPassword@123',
        })

        self.assertEqual(response.status_code, 302)

    def test_invalid_login(self):
        response = self.client.post(reverse('login'), {
            'username': 'wronguser',
            'password': 'wrongpassword',
        })

        self.assertEqual(response.status_code, 200)

    def test_dashboard_requires_login(self):
        response = self.client.get(reverse('student_dashboard'))

        self.assertEqual(response.status_code, 302)

    def test_dashboard_after_login(self):
        user = User.objects.create_user(
            username='sayali',
            password='TestPassword@123'
        )

        self.client.login(
            username='sayali',
            password='TestPassword@123'
        )

        response = self.client.get(reverse('student_dashboard'))

        self.assertEqual(response.status_code, 200)

    def test_user_logout(self):
        User.objects.create_user(
            username='sayali',
            password='TestPassword@123'
        )

        self.client.login(
            username='sayali',
            password='TestPassword@123'
        )

        response = self.client.get(reverse('logout'))

        self.assertEqual(response.status_code, 302)