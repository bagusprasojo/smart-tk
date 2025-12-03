from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, UpdateView

from core.mixins import RoleRequiredMixin
from .forms import ArticleForm
from .models import Article


class PublicArticleListView(ListView):
    template_name = 'articles/article_list.html'
    context_object_name = 'articles'
    model = Article

    def get_queryset(self):
        return Article.objects.filter(status=Article.Status.PUBLISHED)


class PublicArticleDetailView(DetailView):
    template_name = 'articles/article_detail.html'
    context_object_name = 'article'
    model = Article

    def get_queryset(self):
        return Article.objects.filter(status=Article.Status.PUBLISHED)


class ArticleManageListView(RoleRequiredMixin, ListView):
    template_name = 'articles/article_manage_list.html'
    context_object_name = 'articles'
    allowed_roles = ['ADMIN', 'GURU']

    def get_queryset(self):
        qs = Article.objects.all()
        user = self.request.user
        if user.role == 'GURU':
            qs = qs.filter(author=user)
        return qs


class ArticleCreateView(RoleRequiredMixin, CreateView):
    template_name = 'articles/article_form.html'
    form_class = ArticleForm
    success_url = reverse_lazy('article_manage_list')
    allowed_roles = ['ADMIN', 'GURU']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ArticleUpdateView(RoleRequiredMixin, UpdateView):
    template_name = 'articles/article_form.html'
    form_class = ArticleForm
    success_url = reverse_lazy('article_manage_list')
    allowed_roles = ['ADMIN', 'GURU']
    model = Article

    def get_queryset(self):
        qs = super().get_queryset()
        if self.request.user.role == 'GURU':
            qs = qs.filter(author=self.request.user)
        return qs
