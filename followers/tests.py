from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Follower


class FollowerListViewTests(APITestCase):
    def setUp(self):
        """
        Automatically runs before every test method
        """
        User.objects.create_user(username='tom', password='password')

    def test_not_logged_in_user_cannot_follow(self):
        """
        Test to ensure logged out user cannot follow others
        """
        response = self.client.post('/followers/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class FollowerDetailViewTests(APITestCase):
    def setUp(self):
        """
        Contains 3 users and 2 follows of 1st and 2nd user
        """
        tom = User.objects.create_user(username='tom', password='password')
        jerry = User.objects.create_user(username='jerry', password='password')
        mike = User.objects.create_user(username='mike', password='password')

        Follower.objects.create(owner=tom, followed_id=2)
        Follower.objects.create(owner=jerry, followed_id=3)

    def test_logged_in_user_can_follow_others(self):
        """
        Test to ensure logged in user can follow others
        """

        self.client.login(username='tom', password='password')
        response = self.client.post('/followers/', {'followed': 3})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_can_retrieve_existing_following(self):
        """
        Test if possible to retrieve a following with a valid ID
        """
        self.client.login(username='tom', password='password')
        response = self.client.get('/followers/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_cannot_retrieve_non_existing_following(self):
        """
        Test if possible to retrieve a following with an invalid ID
        """
        self.client.login(username='tom', password='password')
        response = self.client.get('/followers/999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_can_unfollow(self):
        """
        Test if user can unfollow user
        """
        self.client.login(username='tom', password='password')
        response = self.client.delete('/followers/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_user_can_unfollow_other_user_follow(self):
        """
        Test if user can remove other user's follow
        """
        self.client.login(username='tom', password='password')
        response = self.client.delete('/followers/2/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
