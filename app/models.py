from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

# Import User Manager
from .managers import CustomUserManager


# User Authentication & Creation Model
# Extended from built in Django User Model
# Replaces Username as a required field to Email
class CustomUser(AbstractUser):
    username = None
    name = models.CharField(max_length=150)
    email = models.EmailField(_('email'), unique=True)
    profile_img = models.URLField(max_length=255, default='https://picsum.photos/id/1005/600/300')

    # Changes the required field for login to 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


# Many-to-One Rel with Custom User
class Post(models.Model):
    title = models.CharField(max_length=30)
    author = models.ForeignKey(CustomUser, related_name='authors', on_delete=models.CASCADE)
    code_block = models.TextField(max_length=600)
    code_notes = models.TextField(max_length=200)
    # Date related attributes
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


# Many-to-One Rel with Post
class Comment(models.Model):
    comment = models.CharField(max_length=150)
    post = models.ForeignKey(Post, related_name='posts', on_delete=models.CASCADE)
    comment_auth = models.ForeignKey(CustomUser, related_name='commenter', on_delete=models.CASCADE)
    # Date related attributes
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


# Many-to-Many Rel with Post
class Category(models.Model):
    cat_name = models.CharField(max_length=30, default='Uncategorized')
    posts = models.ManyToManyField(Post, related_name='post_cats')
    # Date related attributes
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
