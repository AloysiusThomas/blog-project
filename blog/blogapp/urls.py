from django.urls import path

from .views import ArticleCreateView
from .views import ArticleDeleteView
from .views import ArticleDetailView
from .views import ArticleListView
from .views import ArticleUpdateView
from .views import download_article

app_name = 'blogapp'

urlpatterns = [
    path("", ArticleListView.as_view(), name='article-list'),
    path("<int:id>/", ArticleDetailView.as_view(), name='article-details'),
    path("create/", ArticleCreateView.as_view(), name='article-create'),
    path("<int:id>/update/", ArticleUpdateView.as_view(), name='article-update'),
    path("<int:id>/delete/", ArticleDeleteView.as_view(), name='article-delete'),
    path('download/<int:article_id>/', download_article, name="download")

]
