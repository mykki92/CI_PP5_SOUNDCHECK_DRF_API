from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Check
from posts.models import Post


class CheckListViewTests(APITestCase):
    def setUp(self):
        """
        Automatically runs before every test method
        """
        User.objects.create_user(username='tom', password='password')

    def test_not_logged_in_user_cannot_check_post(self):
        """
        Test to ensure logged out user cannot check post
        """
        response = self.client.post('/checks/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class CheckDetailViewTests(APITestCase):
    def setUp(self):
        """
        Contains two users, 3 posts and 2 checks for 1st and 2nd post
        """
        tom = User.objects.create_user(username='tom', password='password')
        jerry = User.objects.create_user(username='jerry', password='password')
        Post.objects.create(
            owner=tom, tags='tag',
            content='test'
        )
        Post.objects.create(
            owner=jerry, tags='tag2',
            content='test2'
        )
        Post.objects.create(
            owner=jerry, tags='tag3',
            content='test3'
        )
        Check.objects.create(owner=tom, post_id=2)
        Check.objects.create(owner=jerry, post_id=1)

    def test_logged_in_user_can_check_post(self):
        """
        Test to ensure logged in user can check a post
        """
        self.client.login(username='tom', password='password')
        response = self.client.post('/checks/', {'post': 3})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_can_retrieve_existing_check(self):
        """
        Test if possible to retrieve a check with a valid ID
        """
        self.client.login(username='tom', password='password')
        response = self.client.get('/checks/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_cannot_retrieve_non_existing_check(self):
        """
        Test if possible to retrieve a check with an invalid ID
        """
        self.client.login(username='tom', password='password')
        response = self.client.get('/checks/999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_can_uncheck_own_check(self):
        """
        Test if user can remove their own check
        """
        self.client.login(username='tom', password='password')
        response = self.client.delete('/checks/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_user_can_uncheck_other_user_check(self):
        """
        Test if user can remove another users check
        """
        self.client.login(username='tom', password='password')
        response = self.client.delete('/checks/2/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
