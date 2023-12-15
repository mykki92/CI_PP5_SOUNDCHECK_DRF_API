from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Follower


class FollowerListViewTests(APITestCase):
    def setUp(self):
        User.objects.create_user(username='tom', password='password')

    def test_not_logged_in_user_cannot_follow(self):
        response = self.client.post('/followers/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class FollowerDetailViewTests(APITestCase):
    def setUp(self):
        tom = User.objects.create_user(username='tom', password='password')
        jerry = User.objects.create_user(username='jerry', password='password')
        mike = User.objects.create_user(username='mike', password='password')

        Follower.objects.create(owner=tom, followed_id=2)
        Follower.objects.create(owner=jerry, followed_id=3)

    def test_logged_in_user_can_follow_others(self):
        self.client.login(username='tom', password='password')
        response = self.client.post('/followers/', {'followed': 3})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_can_retrieve_existing_following(self):
        self.client.login(username='tom', password='password')
        response = self.client.get('/followers/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_cannot_retrieve_non_existing_following(self):
        self.client.login(username='tom', password='password')
        response = self.client.get('/followers/999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_can_unfollow(self):
        self.client.login(username='tom', password='password')
        response = self.client.delete('/followers/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_user_can_unfollow_other_user_follow(self):
        self.client.login(username='tom', password='password')
        response = self.client.delete('/followers/2/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
