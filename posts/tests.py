from django.contrib.auth.models import User
from .models import Post
from rest_framework import status
from rest_framework.test import APITestCase


class PostListViewTests(APITestCase):
    def setUp(self):
        """
        Automatically runs before every test method
        """
        User.objects.create_user(username='tom', password='password')

    def test_can_list_posts(self):
        """
        Test that posts present in the database can be listed
        """
        tom = User.objects.get(username='tom')
        Post.objects.create(owner=tom, tags='tag')
        response = self.client.get('/posts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data)
        print(len(response.data))

    def test_logged_in_user_can_create_post(self):
        """
        Test to ensure logged in user can create a post
        """
        self.client.login(username='tom', password='password')
        response = self.client.post('/posts/', {'tags': 'tag'})
        count = Post.objects.count()
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_not_logged_in_cant_create_post(self):
        """
        Test to ensure logged out user cannot create a post
        """
        response = self.client.post('/posts/', {'tags': 'tag'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class PostDetailViewTests(APITestCase):
    def setUp(self):
        """
        Contains two users with a post for each user
        """
        tom = User.objects.create_user(username='tom', password='password')
        jerry = User.objects.create_user(username='jerry', password='password')
        Post.objects.create(
            owner=tom, tags='tag', caption='toms caption'
        )
        Post.objects.create(
            owner=jerry, tags='tag', caption='jerrys caption'
        )

    def test_can_retrieve_post_using_valid_id(self):
        """
        Test if possible to retrieve a post with a valid ID
        """
        response = self.client.get('/posts/1/')
        self.assertEqual(response.data['tags'], 'tag')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cant_retrieve_post_using_invalid_id(self):
        """
        Test if possible to retrieve a post with an invalid ID)
        """
        response = self.client.get('/posts/999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_can_update_own_post(self):
        """
        Test if user can update a post they own
        """
        self.client.login(username='tom', password='password')
        response = self.client.put('/posts/1/', {'tags': 'tag'})
        post = Post.objects.filter(pk=1).first()
        self.assertEqual(post.tags, 'tag')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_cant_update_another_users_post(self):
        """
        Test if user can update other users' posts
        """
        self.client.login(username='tom', password='password')
        response = self.client.put('/posts/2/', {'tags': 'tag'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
