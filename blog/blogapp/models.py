from django.contrib.auth.models import AbstractUser
from django.db import models

from blogapp.utils import article_extra_image_location
from blogapp.utils import article_image_location


class Article(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    active = models.BooleanField(default=True)
    top_image = models.ImageField(upload_to=article_image_location)
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return "/blog/%s" % self.id

    def __str__(self):
        return self.title


class ArticleImage(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, default=None)
    image = models.ImageField(upload_to=article_extra_image_location)


class User(AbstractUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    nick_name = models.CharField(max_length=128, blank=True, null=True)

    def __str__(self):
        return self.get_full_name()
