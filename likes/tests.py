from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Check
from posts.models import Post


class LikeListViewTests(APITestCase):
    def setUp(self):
        """
        Automatically runs before every test method
        """
        User.objects.create_user(username='tom', password='password')

    def test_not_logged_in_user_cannot_like_post(self):
        """
        Test to ensure logged out user cannot like post
        """
        response = self.client.post('/likes/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class LikeDetailViewTests(APITestCase):
    def setUp(self):
        """
        Contains two users, 3 posts and 2 like for 1st and 2nd post
        """
        tom = User.objects.create_user(username='tom', password='password')
        jerry = User.objects.create_user(username='jerry', password='password')
        Post.objects.create(
            owner=tom, title='post title',
            content='test'
        )
        Post.objects.create(
            owner=jerry, title='post title2',
            content='test2'
        )
        Post.objects.create(
            owner=jerry, title='post title3',
            content='test3'
        )
        Like.objects.create(owner=tom, post_id=2)
        Like.objects.create(owner=jerry, post_id=1)

    def test_logged_in_user_can_like_post(self):
        """
        Test to ensure logged in user can like a post
        """
        self.client.login(username='tom', password='password')
        response = self.client.post('/likes/', {'post': 3})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_can_retrieve_existing_like(self):
        """
        Test if possible to retrieve a like with a valid ID
        """
        self.client.login(username='tom', password='password')
        response = self.client.get('/likes/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_cannot_retrieve_non_existing_like(self):
        """
        Test if possible to retrieve a like with an invalid ID
        """
        self.client.login(username='tom', password='password')
        response = self.client.get('/likes/999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_can_unlike_own_like(self):
        """
        Test if user can remove their own like
        """
        self.client.login(username='tom', password='password')
        response = self.client.delete('/likes/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_user_can_unlike_other_user_like(self):
        """
        Test if user can remove another users like
        """
        self.client.login(username='tom', password='password')
        response = self.client.delete('/likes/2/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
