from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse


class MyUserRegisterTest(TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        # valid user data
        cls.user_data = {
            'username': 'otus',
            'email': 'admin@otus.local',
            'password1': 'OtusOtus',
            'password2': 'OtusOtus',
        }
        # bad user data
        cls.user_bad_data = {
            'username': 'otus',
            'email': 'admin@otus.local',
            'password1': 'OtusOtus',
            'password2': 'Otus',
        }

    def test_register_ok(self):

        response = self.client.get('/auth/register/')
        self.assertIn('Username:', response.content.decode())
        self.assertEqual(200, response.status_code)

        # post
        response = self.client.post('/auth/register/', data=self.user_data)
        self.assertEqual(302, response.status_code)

        # check user
        new_user = get_user_model().objects.get(
            username=self.user_data['username']
        )

        self.assertEqual(
            self.user_data['email'],
            new_user.email,
        )

    def test_register_fail(self):
        response = self.client.post(
            reverse('register'),
            data=self.user_bad_data,
        )
        self.assertEqual(200, response.status_code)
        self.assertFormError(
            response,
            'form',
            'password2',
            'The two password fields didn’t match.')
