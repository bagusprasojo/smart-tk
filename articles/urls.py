from django.urls import path

from .views import (
    ArticleCreateView,
    ArticleManageListView,
    ArticleUpdateView,
    PublicArticleDetailView,
    PublicArticleListView,
)

urlpatterns = [
    path('', PublicArticleListView.as_view(), name='article_list'),
    path('<int:pk>/', PublicArticleDetailView.as_view(), name='article_detail'),
    path('manage/', ArticleManageListView.as_view(), name='article_manage_list'),
    path('manage/add/', ArticleCreateView.as_view(), name='article_add'),
    path('manage/<int:pk>/edit/', ArticleUpdateView.as_view(), name='article_edit'),
]
