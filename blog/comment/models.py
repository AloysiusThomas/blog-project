from django.contrib.auth import get_user_model
from django.db import models

from blogapp.models import Article


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    comment = models.TextField()
    added_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    added_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    edited = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.added_on and self.updated_on:
            if self.added_on < self.updated_on:
                self.edited = True

        super(Comment, self).save()

    def __str__(self):
        return f"Comment by {str(self.added_by)}"
