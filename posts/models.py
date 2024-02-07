from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    """
    A class for the post model
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    caption = models.TextField(blank=True)
    tags = models.CharField(max_length=255)
    post_image = models.ImageField(
        upload_to='images/', default='../soundcheck_default_post', blank=True
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.tags}'
