from django.contrib.auth.models import AbstractUser
from django.db import models


def article_image_location(instance, filename):
    try:
        extension = filename.split(".")[1].lower()
        extension = "." + extension
    except Exception as e:
        print(e, "Handled")
        extension = ""
    filename = str(instance.title)
    filename = filename.replace(" ", "-")
    filename = filename + extension
    location = "article/images/"
    return '%s/%s' % (location, filename)


class Article(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    active = models.BooleanField(default=True)
    image = models.ImageField(upload_to=article_image_location)
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return "/blog/%s" % self.id

    def __str__(self):
        return self.title


class User(AbstractUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    nick_name = models.CharField(max_length=128, blank=True, null=True)

    def __str__(self):
        return self.get_full_name()
