from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test create a new user with an email is successful"""
        email = 'behroozghamami@gmail.com'
        password = 'admin1234'
        user = get_user_model().objects.create_user(
            email=email,
            password=password,

        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """test new user email is normalized"""
        email = 'behroozghamami@GMAIL.COM'
        user = get_user_model().objects.create_user(email, 'admin1234')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test create user with invalid email raises error"""

        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'admin1234')

    def test_create_new_superuser(self):
        """test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            'behroozghamami@gmail.com',
            'admin1234'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
