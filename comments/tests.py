from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Comment
from posts.models import Post


class CommentListViewTests(APITestCase):
    """
        Automatically runs before every test method
    """
    def setUp(self):
        User.objects.create_user(username='tom', password='password')
    """
        Test to ensure logged out user cannot create a comment
    """
    def test_not_logged_in_user_cannot_create_comment(self):
        response = self.client.post('/comments/', {'content': 'a comment'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class CommentDetailViewTests(APITestCase):
    def setUp(self):
        """
        Contains two users with post and comments for each
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
        Comment.objects.create(owner=tom, post_id=1, content='comment one')
        Comment.objects.create(owner=jerry, post_id=2, content='comment two')

    def test_logged_in_user_can_create_comment(self):
        """
        Test to ensure logged in user can create a comment
        """
        self.client.login(username='tom', password='password')
        response = self.client.post('/comments/', {'post': 1,
                                                   'content': 'a new comment'})
        comment_count = Comment.objects.count()
        self.assertEqual(comment_count, 3)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_can_retrieve_existing_comment(self):
        """
        Test if possible to retrieve a comment with a valid ID
        """
        self.client.login(username='tom', password='password')
        response = self.client.get('/comments/1/')
        self.assertEqual(response.data['content'], 'comment one')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cannot_retrieve_non_existing_comment(self):
        """
        Test if possible to retrieve a comment with an invalid ID
        """
        self.client.login(username='tom', password='password')
        response = self.client.get('/comments/9999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_can_update_their_own_comment(self):
        """
        Test if user can update a comment they created
        """
        self.client.login(username='tom', password='password')
        response = self.client.put('/comments/1/',
                                   {'content': 'updated comment'})
        comment = Comment.objects.filter(pk=1).first()
        self.assertEqual(comment.content, 'updated comment')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_cannot_update_other_users_comment(self):
        """
        Test if user can update other users' comment
        """
        self.client.login(username='tom', password='password')
        response = self.client.put('/comments/2/',
                                   {'content': 'updated comment'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_user_can_delete_their_own_comment(self):
        """
        Test if user can delete their own comment
        """
        self.client.login(username='tom', password='password')
        response = self.client.delete('/comments/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_user_cannot_delete_other_users_comment(self):
        """
        Test if user can delete other users' comment
        """
        self.client.login(username='tom', password='password')
        response = self.client.delete('/comments/2/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
