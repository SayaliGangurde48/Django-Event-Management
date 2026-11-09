from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import EventUpload


class EventUploadTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='sayali',
            password='TestPassword@123'
        )

        self.client.login(
            username='sayali',
            password='TestPassword@123'
        )

    def test_upload_page(self):
        response = self.client.get(reverse('upload_event'))

        self.assertEqual(response.status_code, 200)

    def test_valid_csv_upload(self):
        csv_file = SimpleUploadedFile(
            'test.csv',
            b'name,score\nSayali,90',
            content_type='text/csv'
        )

        response = self.client.post(reverse('upload_event'), {
            'event_type': 'Hackathon',
            'event_date': '2026-11-09',
            'csv_file': csv_file,
        })

        self.assertEqual(response.status_code, 302)

        self.assertEqual(
            EventUpload.objects.filter(student=self.user).count(),
            1
        )

    def test_non_csv_upload(self):
        file = SimpleUploadedFile(
            'test.txt',
            b'This is a text file',
            content_type='text/plain'
        )

        response = self.client.post(reverse('upload_event'), {
            'event_type': 'Workshop',
            'event_date': '2026-11-09',
            'csv_file': file,
        })

        self.assertEqual(response.status_code, 200)
        self.assertEqual(EventUpload.objects.count(), 0)

    def test_empty_csv_upload(self):
        file = SimpleUploadedFile(
            'empty.csv',
            b'',
            content_type='text/csv'
        )

        response = self.client.post(reverse('upload_event'), {
            'event_type': 'Internship',
            'event_date': '2026-11-09',
            'csv_file': file,
        })

        self.assertEqual(response.status_code, 200)
        self.assertEqual(EventUpload.objects.count(), 0)

    def test_file_larger_than_5mb(self):
        file = SimpleUploadedFile(
            'large.csv',
            b'a' * (6 * 1024 * 1024),
            content_type='text/csv'
        )

        response = self.client.post(reverse('upload_event'), {
            'event_type': 'Orientation',
            'event_date': '2026-11-09',
            'csv_file': file,
        })

        self.assertEqual(response.status_code, 200)
        self.assertEqual(EventUpload.objects.count(), 0)

    def test_upload_requires_login(self):
        self.client.logout()

        response = self.client.get(reverse('upload_event'))

        self.assertEqual(response.status_code, 302)