from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Profile


class ProfileDetailViewTests(APITestCase):
    def setUp(self):
        """
        Creates two user instances
        """
        User.objects.create_user(username='tom',
                                 password='password')
        User.objects.create_user(username='jerry',
                                 password='password')

    def test_user_can_view_existing_profile(self):
        """
        Test if possible to view existing profile with a valid ID
        """
        self.client.login(username='tom', password='password')
        response = self.client.get('/profiles/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_cannot_view_non_existing_profile(self):
        """
        Test if possible to view a profile with an invalid ID
        """
        self.client.login(username='tom', password='password')
        response = self.client.get('/profiles/9999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_can_update_owned_profile(self):
        """
        Test if user can update a profile they own
        """
        self.client.login(username='tom', password='password')
        response = self.client.put('/profiles/1/',
                                   {'name': 'thomas'})
        profile = Profile.objects.filter(pk=1).first()
        self.assertEqual(profile.name, 'thomas')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_cannot_update_other_profiles(self):
        """
        Test if user can update other users profiles
        """
        self.client.login(username='tom', password='password')
        response = self.client.put('/profiles/2/', {'name': 'thomas'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_un_auth_user_can_update_owned_profile(self):
        """
        Test if user can update their profile when not logged in
        """
        response = self.client.put('/profiles/1/',
                                   {'name': 'thomas'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def tearDown(self):
        Profile.objects.all().delete()
        User.objects.all().delete()
