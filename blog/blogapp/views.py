from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView
from django.views.generic import DeleteView
from django.views.generic import ListView
from django.views.generic import UpdateView
from django.views.generic.base import View

from comment.forms import CommentForm
from comment.models import Comment
from .forms import ArticleModelForm
from .models import Article


class ArticleObjectMixin(object):
    model = Article

    def get_object(self, queryset=None):
        pk = self.kwargs.get("id")
        return get_object_or_404(self.model, id=pk)


class ArticleCreateView(CreateView):
    form_class = ArticleModelForm
    template_name = 'blogapp/article_create.html'

    def get_success_url(self):
        success_url = "/blog/"
        return success_url


class ArticleListView(ListView):
    queryset = Article.objects.all().order_by('-id')


class ArticleDetailView(ArticleObjectMixin, View):
    template_name = "blogapp/article_detail.html"
    context = dict()

    def get(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj is not None:
            form = CommentForm(request.POST)
            self.context['form'] = form
            self.context['object'] = obj
            c = Comment.objects.filter(article=obj).order_by('-id')

            self.context['comments'] = c

        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj is not None:
            form = CommentForm(request.POST)
            if form.is_valid():
                s = form.save(commit=False)
                s.article = obj
                try:
                    s.added_by = request.user
                except Exception as e:
                    print(e)
                    return redirect('login')
                s.save()
                return HttpResponseRedirect(f'/blog/{obj.id}')
            c = Comment.objects.filter(article=obj).order_by('-id')
            self.context['object'] = obj
            self.context['comments'] = c
            self.context['form'] = form

        return render(request, self.template_name, self.context)


class ArticleUpdateView(UpdateView):
    form_class = ArticleModelForm
    template_name = 'blogapp/article_create.html'

    def get_object(self, queryset=None):
        pk = self.kwargs.get("id")
        return get_object_or_404(Article, id=pk)

    def get_success_url(self):
        success_url = "/blog/"
        return success_url


class ArticleDeleteView(DeleteView):
    success_url = "/blog/"

    def get_object(self, queryset=None):
        pk = self.kwargs.get("id")
        return get_object_or_404(Article, id=pk)
