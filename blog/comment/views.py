from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import UpdateView

from comment.forms import CommentForm
from comment.models import Comment


class ArticleUpdateView(UpdateView):
    form_class = CommentForm
    template_name = 'comment/edit_comment.html'

    def get_object(self, queryset=None):
        pk = self.kwargs.get("id")
        return get_object_or_404(Comment, id=pk)

    def get_success_url(self):
        success_url = "/blog/"
        return success_url

